#!/usr/bin/env python
from setuptools import setup

with open('requirements.txt') as f:
    packages = f.read().splitlines()

setup(install_requires=packages)
