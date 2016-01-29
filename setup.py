#!/usr/bin/env python

from distutils.core import setup

setup(
    name='scikit-ribo',
    version='0.1.0',
    author='Han Fang',
    author_email='hanfang.cshl@gmail.com',
    packages=['scikit-ribo', 'scikit-ribo.test'],
    scripts=['script/bam_preprocess.py','script/gtf_preprocess.py'],
    url='http://pypi.python.org/pypi/scikit-ribo/',
    license='LICENSE.txt',
    description='A scikit framework for joint analysis of Riboseq and RNAseq data.',
    long_description=open('docs/README.txt').read(),
    install_requires=[
    ],
)