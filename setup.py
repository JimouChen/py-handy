# !/usr/bin/env python3
# _*_ coding: utf-8 _*_
from os import path

from setuptools import setup, find_packages

with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyhandytools',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/JimouChen/py-handy',
    author='Jimou Chen',
    author_email='neaya1024@gmail.com',
    description='Python handy tools',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['toolbox', 'kit', 'utils', 'tools'],
    install_requires=[
        'loguru'
    ]
)
