import sys
from codecs import open
from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

assert sys.version_info[0] == 3, "steepdata requires Python > 3"

VERSION = '0.0.1'

setup(
    name='steepdata',
    version=VERSION,
    description='Python Utilities for parsing STEEM blockchain',
    long_description=open('README.md').read(),
    url='https://github.com/Chainers/steepdata',
    author='by SteepShot team',
    author_email='steepshot.org@gmail.com',
    license=open('LICENSE.txt').read(),
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='steem steemit steepdata',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=[
        'steep-steem',
        'pymongo',
        'python-dateutil',
        'requests',
        'funcy',
        'werkzeug',
    ],

    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
)
