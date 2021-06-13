# aioservertiming

[![PyPi Package Version](https://img.shields.io/pypi/v/aioservertiming.svg)](https://pypi.python.org/pypi/aioservertiming)
[![Supported python versions](https://img.shields.io/pypi/pyversions/aioservertiming.svg)](https://pypi.python.org/pypi/aioservertiming)

The *Server-Timing* header communicates one or more metrics and descriptions for a given request-response cycle. It is used to surface any backend server timing metrics (e.g. database read/write, CPU time, file system access, etc.) in the developer tools in the user's browser or in the [PerformanceServerTiming](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceServerTiming) interface. *aioservertiming* provides conventient functions to work with it from aiohttp.

## Installation

Installation process as simple as:

    $ pip install aioservertiming

## Usage

First we need to set a middleware to app.

```python3
from aiohttp import web
from aioservertiming import server_timing_mware

app = web.Applicalion(
    middlewares = [
        server_timing_mware
    ]
)
```

### Decorator

```python3
import time
from aioservertiming import server_timing

# you can specify both timer name and description
@server_timing(name='test_function')
def test1():
    time.sleep(1)

@server_timing  # if you do not specify timer name than name of function
                # will be used for timer name
def test2():
    time.sleep(2)
```

### Context manager

```python3
from asyncio import sleep

from aiohttp import web
from aioservertiming import server_timing_cm


async def handler(request: web.Request) -> web.Response:
    # timer name must be specified!
    with server_timing_cm('test1'):
        await sleep(0.1)
        
    # you can specify a description for timer
    with server_timing_cm(name='test2', description='testtimerno2'):
        await sleep(0.5)
    return web.Response()
```

## Links

[MDN documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Server-Timing) for Server-Timing

This library on [PyPI](https://pypi.org/project/aioservertiming/)
