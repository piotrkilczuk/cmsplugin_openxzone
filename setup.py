#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name='cmsplugin_openxzone',
    version='0.2.0',
    author='Piotr Kilczuk',
    author_email='piotr@hint.pl',
    #url='http://hint.pl/',
    description = 'A Django CMS - OpenX brigde',
    packages = ['cmsplugin_openxzone',],
    package_data={'cmsplugin': ['templates/*',]},
    provides=['cmsplugin_openxzone',],
)
