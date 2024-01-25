import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="realtime-trains",
    version="0.0.1",
    description="Unofficial Python API for Realtime Trains",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/mbukovac/realtime-trains",
    author="Marko Bukovac",
    author_email="marko.bukovac@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["realtime_trains"],
    include_package_data=True,
    install_requires=["httpx", "pydantic"]
)