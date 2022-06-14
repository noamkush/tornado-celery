#!/usr/bin/env python
import os
import re

from setuptools import setup, find_packages

version = re.compile(r'VERSION\s*=\s*\((.*?)\)')


def get_package_version():
    """returns package version without importing it"""
    base = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(base, "tcelery/__init__.py")) as initf:
        for line in initf:
            m = version.match(line.strip())
            if not m:
                continue
            return ".".join(m.groups()[0].split(", "))


classes = """
    Development Status :: 3 - Alpha
    Intended Audience :: Developers
    License :: OSI Approved :: BSD License
    Topic :: System :: Distributed Computing
    Programming Language :: Python
    Programming Language :: Python :: 2
    Programming Language :: Python :: 2.6
    Programming Language :: Python :: 2.7
    Programming Language :: Python :: 3
    Programming Language :: Python :: 3.2
    Programming Language :: Python :: 3.3
    Programming Language :: Python :: Implementation :: CPython
    Operating System :: OS Independent
"""
classifiers = [s.strip() for s in classes.split('\n') if s]

setup(
    name='tornado-celery',
    version=get_package_version(),
    description='Celery integration with Tornado',
    long_description=open('README.rst').read(),
    author='Mher Movsisyan',
    author_email='mher.movsisyan@gmail.com',
    url='https://github.com/mher/tornado-celery',
    license='BSD',
    classifiers=classifiers,
    packages=find_packages(exclude=['tests', 'tests.*']),
    install_requires=['celery', 'tornado', 'pika'],
    extras_require={
        'redis': ["tornado-redis"]
    },
    entry_points={
        'console_scripts': [
            'tcelery = tcelery.__main__:main',
        ]
    },
)
