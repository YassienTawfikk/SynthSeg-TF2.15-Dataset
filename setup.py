#!/usr/bin/env python

import sys
import setuptools

else:

    with open('requirements.txt') as f:
        required_packages = [line.strip() for line in f.readlines()]

    print(setuptools.find_packages())

    setuptools.setup(name='SynthSeg',
                     version='2.0',
                     license='Apache 2.0',
                     description='Domain-agnostic segmentation of brain scans',
                     author='Benjamin Billot',
                     url='https://github.com/GabrieleLozupone/SynthSeg-TF2.15-Dataset',
                     keywords=['segmentation', 'domain-agnostic', 'brain'],
                     packages=setuptools.find_packages(),
                     python_requires='>=3.11',
                     install_requires=required_packages,
                     include_package_data=True)
