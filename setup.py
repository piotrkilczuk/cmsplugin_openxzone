#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name='cmsplugin_openxzone',
    version='0.1.2',
    author='Piotr Kilczuk',
    author_email='piotr@hint.pl',
    #url='http://hint.pl/',
    description = 'A Django CMS - OpenX brigde',
    packages = ['cmsplugin_openxzone',],
    package_data={'cmsplugin': ['templates/*',]},
    provides=['cmsplugin_openxzone',],
    install_requires = ['django-inline-ordering>=0.1.1', 'easy-thumbnails',]
)
