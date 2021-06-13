import time
from typing import Optional
from contextlib import contextmanager
from contextvars import ContextVar
from dataclasses import dataclass
from functools import wraps

from aiohttp import web
from aiohttp.web_middlewares import _Handler as Handler


server_timings = ContextVar("timings")


@dataclass
class Timer:

    name: str
    description: Optional[str] = None
    duration: float = 0

    __stopped = False

    def start(self):
        self.__start = time.time()

    def stop(self):
        if self.is_stopped:
            raise RuntimeError("Timer is already stopped")
        self.duration = time.time() - self.__start

    @property
    def is_stopped(self):
        return self.__stopped

    def __post_init__(self):
        if " " in self.name:
            raise ValueError("Whitespace in server timing name")
        if self.description and " " in self.description:
            self.description = f'"{self.description}"'

    def __str__(self) -> str:
        base = f"{self.name}"
        if self.description:
            base += f";desc={self.description}"
        if self.duration:
            base += f";dur={self.duration:.3f}"
        return base

    def __repr__(self):
        clsname = self.__class__.__name__
        return f"{clsname}({self})"


@web.middleware
async def server_timing_mware(
    request: web.Request,
    handler: Handler
) -> web.StreamResponse:
    server_timings.set([])
    response = await handler(request)
    raw_timings = server_timings.get()
    if raw_timings:
        server_timing_str = ", ".join(map(str, raw_timings))
        response.headers["Server-Timing"] = server_timing_str
    return response


@contextmanager
def server_timing_cm(name: str, description: Optional[str] = None):
    timings = server_timings.get()
    if timings and not timings[-1].is_stopped():
        raise RuntimeError("Nested server timers")
    timer = Timer(name=name, description=description)
    timings.append(timer)
    timer.start()
    try:
        yield
    finally:
        timer.stop()


def server_timing(name: Optional[str] = None, description: Optional[str] = None):

    def wrapper(fn):
        if not name:
            timer_name = name or fn.__name__

        @wraps(fn)
        def wrapped(*args, **kwargs):
            with server_timing_cm(timer_name, description):
                return fn(*args, **kwargs)
        return wrapped
    return wrapper
