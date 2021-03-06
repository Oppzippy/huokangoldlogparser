#!/usr/bin/env python3

from distutils.core import setup
import setuptools

setup(
    name="huokangoldlogparser",
    version="1.0.0",
    description="Parses gold logs produced by HuokanGoldLogger",
    author="Oppzippy",
    author_email="oppzippy@gmail.com",
    license="UNLICENSED",
    packages=setuptools.find_packages(),
    install_requires=["python-dateutil"],
    entry_points={
        "console_scripts": ["huokangoldlogparser=cli.huokangoldlogparser:main"]
    },
)
