# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in flycrown/__init__.py
from flycrown import __version__ as version

setup(
	name='flycrown',
	version=version,
	description='customization needed in crown project',
	author='ARD',
	author_email='hadeel.milad@ard.ly',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
