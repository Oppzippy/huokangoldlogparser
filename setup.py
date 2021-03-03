#!/usr/bin/env python3

from distutils.core import setup
import setuptools

setup(
    name="huokangoldlogparser",
    version="0.0.4",
    description="Parses gold logs produced by HuokanGoldLogger",
    author="Oppzippy",
    packages=setuptools.find_packages(),
    scripts=["huokangoldlogparser.py"],
    install_requires=["python-dateutil"],
)
