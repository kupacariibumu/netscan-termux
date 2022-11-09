#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(name='netscan-termux',
      version='2.0',
      description='Netscan Termux',
      url='https://github.com/mrpontora/netscan-termux',
      author='MR PONTORA',
      author_email='mr.pontora@gmail.com',
      packages=['source'],
      install_requires=['requests==2.21.0'],
      python_requires=">=3",
      zip_safe=False)