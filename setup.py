#!/usr/bin/env python

from setuptools import find_packages, setup

setup(name='kivy3',
      version='0.1',
      description='Kivy extensions for 3D graphics',
      author='Niko Skrypnik',
      author_email='nskrypnik@gmail.com',
      packages=find_packages(exclude=("tests",)),
      requires=['kivy', ]
    )
