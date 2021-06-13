import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aioservertiming",
    version="0.0.1a1",
    author="jorektheglitch",
    author_email="jorektheglitch@yandex.ru",
    description="Server Timing interaction for aiohttp",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jorektheglitch/aioservertiming",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
