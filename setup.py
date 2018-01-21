#-*- coding:utf-8 -*-
"""
Setup for baguette utils package.
"""
from setuptools import find_packages, setup

setup(
    name='baguette-utils',
    version='0.14',
    description='some dummy wrappers',
    keywords=['utils', 'request'],
    url='https://github.com/baguette-io/baguette-utils/',
    author='pydavid',
    author_email='pydavid@baguette.io',
    packages=find_packages(),
    platforms=[
        'Linux/UNIX',
        'MacOS',
        'Windows'
    ],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'requests==2.14.2',
    ],
    extras_require={
        'testing': [
            'mock==2.0.0',
            'pytest==2.9.2',
            'pytest-cov==2.3.0',
            'pylint==1.6.1',
        ],
        'doc': [
            'Sphinx==1.4.4',
        ],
    },
)
