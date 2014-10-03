#!/usr/bin/env python

import sys
from setuptools import setup

DESC = """A Python Package to infer ages using US Census Data"""

LONG_DESC = open("README.md").read()

setup(
    name="demographica",
    version='0.1',
    description=DESC,
    long_description=LONG_DESC,
    author="Cameron Davidson-Pilon",
    author_email="cam.davidson.pilon@gmail.com",
    license="MIT",
    packages=["demographica"],
    url="https://github.com/CamDavidsonPilon/demographica",
    install_requires=["numpy", "pandas>=0.14", "matplotlib"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering",
    ],
)
