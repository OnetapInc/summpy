#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
import os
import codecs


long_description = ''
if os.path.exists('README.rst'):
    long_description = codecs.open('README.rst', encoding='utf-8').read()

setup(
    name='summpy-fix',
    version='1.0.0',
    description='Text summarization (sentence extraction) module with simple HTTP API. (currently, supports Japanese only)',
    long_description=long_description,
    author='OnetapInc',
    author_email='onetap0507@gmail.com',
    license='MIT',
    url='https://github.com/OnetapInc/summpy-fix',
    packages=['summpy-fix', 'summpy.misc'],
    package_data={'summpy-fix': ['server_data/*.html']},
    install_requires=[
        'numpy', 'scipy', 'scikit-learn', 'networkx', 'cherrypy'
    ],
    keywords=[
        'automatic summarization',
        'natural language processing'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7'
    ]
)
