# -*- coding: utf-8 -*-

# https://github.com/andreasmherman/PerfectPythonPackage

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='The Perfect Project',
    version='0.1.0',
    description='A simple project structure.',
    long_description=readme,
    author='Andreas Herman',
    author_email='andreas.m.herman@gmail.com',
    url='https://github.com/andreasmherman/PerfectPythonPackage',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
