#!/usr/bin/env python3

from distutils.core import setup

setup(
    name="HuokanGoldLogger-Parser",
    version="0.0.1",
    description="Parses gold logs produced by HuokanGoldLogger",
    author="Oppzippy",
    packages=["huokangoldlogger-parser"],
    requires=["python-dateutil"],
)
