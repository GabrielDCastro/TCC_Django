#!/usr/bin/env python
from setuptools import setup, find_packages

requires = [
        'django',
        'pillow',
        'gunicorn',
        'django-heroku'
        ]

setup(name='mysite',
      version='1.0',
      packages=find_packages(),
      install_requires=requires)


