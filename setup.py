import setuptools

from aioservertiming import __version__


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aioservertiming",
    version=__version__,
    author="jorektheglitch",
    author_email="jorektheglitch@yandex.ru",
    description="Server Timing interaction for aiohttp",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jorektheglitch/aioservertiming",
    packages=setuptools.find_packages(),
    install_requires=[
        'aiohttp'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
