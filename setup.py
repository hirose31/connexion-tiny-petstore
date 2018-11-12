# coding: utf-8

from setuptools import setup, find_packages
from os import path
import re

NAME = "connexion-tiny-petstore"

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

with open(
        path.join(
            path.dirname(__file__),
            'tiny_petstore', '__init__.py')) as v_file:
    VERSION = re.compile(
        r".*__version__ = '(.*?)'",
        re.S).match(v_file.read()).group(1)

setup(
    name=NAME,
    version=VERSION,
    description="Connexion Example / Tiny Pet Store",
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url="https://github.com/hirose31/connexion-tiny-petstore",
    license='MIT',

    author='HIROSE Masaaki',
    author_email="hirose31@gmail.com",

    classifiers=[
                 'Development Status :: 3 - Alpha',
                 'Intended Audience :: Developers',
                 "License :: OSI Approved :: MIT License",
                 "Programming Language :: Python",
                 "Programming Language :: Python :: 3.5",
                 "Programming Language :: Python :: 3.6",
                 "Programming Language :: Python :: 3.7",
    ],

    keywords=["Swagger", "Swagger Petstore", "Connexion"],

    packages=find_packages(exclude=['etc', 'var', 'junk']),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,

    install_requires=['connexion'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
