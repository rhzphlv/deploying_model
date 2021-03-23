#!/usr/bin/env python
# -*-coding: utf-8 -*-

import io
import os
from pathlib import Path

from setuptools import find_packages, setup

# Package meta-data
NAME = 'deployment_model'
DESCRIPTION = 'Deploy houseprice model'
URL = 'https://github.com/rhzphlv/deployment_model'
EMAIL = 'rhzphlvi@gmail.com'
AUTHOR = 'rhzphl'
REQUIRES_PYTHON = '>=3.6.0'

# Package required for this module
def list_req(fname='requirements.txt'):
	with open(fname) as file:
		return file.read().splitlines()

file_name = os.path.abspath(os.path.dirname(__file__))
try:
	with io.open(os.path.join(file_name,'README.md'),encoding='utf-8') as f:
		long_description = '\n' + f.read()
except FileNotFoundError:
	long_description = DESCRIPTION


ROOT_DIR = Path(__file__).resolve().parent
PACKAGE_DIR = ROOT_DIR / NAME
about = {}

with open(PACKAGE_DIR/'VERSION') as f:
	_version = f.read().strip()
	about['__version__'] = _version

setup(
	name = NAME,
	version = about['__version__'],
	description = DESCRIPTION,
	long_description = long_description,
	long_description_content_type = 'text/markdown',
	author = AUTHOR,
	python_requires = REQUIRES_PYTHON,
	url = URL,
	packages = find_packages(exclude=('tests',)),
	package_data = {'deployment_model': ['VERSION']},
	install_requires = list_req(),
	extras_require = {},
	include_package_data = True,
	lisence = 'MIT',
	classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
