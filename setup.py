#!/usr/bin/env python

import sys
import os
from setuptools import setup

DESC = """A Python Package to infer ages using US Census Data"""

setup(
    name="demographica",
    version='0.2.4.1',
    description=DESC,
    long_description=DESC,
    author="Cameron Davidson-Pilon",
    author_email="cam.davidson.pilon@gmail.com",
    license="MIT",
    packages=["demographica"],
    url="https://github.com/CamDavidsonPilon/demographica",
    install_requires=["numpy", "pandas>=0.14"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering",
    ],
    package_dir={'demographica':'demographica'},
    package_data={
        "demographica": [
            "../README.md",
            "../LICENSE",
            "datasets/*",
        ]
    },
)
