#!/usr/bin/env python

from setuptools import setup, find_packages
import subprocess

setup(name="realit-singer-encodings",
      version='2.1.0',
      description="Singer.io encodings library",
      python_requires=">=3.8, <3.13",
      author="Stitch",
      keywords = ["singer", "meltano", "pipelinewise", "framework"]
      classifiers = [
          "License :: OSI Approved :: Apache Software License",
          # Specify the Python versions you support here.
          "Programming Language :: Python :: 3.8",
          "Programming Language :: Python :: 3.9",
          "Programming Language :: Python :: 3.10",
          "Programming Language :: Python :: 3.11",
          "Programming Language :: Python :: 3.12",
          "Development Status :: 5 - Production/Stable", "Topic :: Database"
      ]
      url="https://github.com/s7clarke10/realit-singer-encodings",
      install_requires=[
      ],
      extras_require={
          "dev": ["nose"]
      },
      packages=['singer-encodings'],
      include_package_data=True
      packages=find_packages(),
)
