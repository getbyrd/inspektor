#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import io
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    with io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ) as fh:
        return fh.read()


test_deps = [
    'flask-testing>=0.7.1',
    'pytest>=4.6.0',
],


setup(
    name='inspektor',
    version='0.1.0',
    license='MIT',
    description='SQLAlchemy querying metrics collection and reporting'
                ' extension for Flask.',
    author='Byrd Technologies GmbH',
    author_email='developers@getbyrd.com',
    url='https://github.com/getbyrd/inspektor',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[
        splitext(basename(path))[0]
        for path in glob('src/*.py')
    ],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries :: Python Modules'
        'Environment :: Web Environment',
    ],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    install_requires=[
        'flask>=1.0',
    ],
    extras_require={
        'test': test_deps
    }
)
