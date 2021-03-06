#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from shutil import rmtree

from setuptools import setup, Command


here = os.path.abspath(os.path.dirname(__file__))

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist bdist_wheel upload")
    sys.exit()

required = [
    'pandocfilters'
]

setup(
    name='pandoc-mermaid-filter',
    version='0.1.0',
    description='Pandoc filter for mermaid code blocks',
    long_description='Pandoc filter for mermaid code blocks',
    author='Timo Furrer',
    author_email='tuxtimo@gmail.com',
    url='https://github.com/Chr1sC0de/pandoc-mermaid-filter',
    install_requires=required,
    py_modules=['pandoc_mermaid_filter'],
    entry_points={
        'console_scripts': [
            'pandoc-mermaid = pandoc_mermaid_filter:main'
        ]},
    license='MIT',
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ),
)
