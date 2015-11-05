#!/usr/bin/python

from setuptools import find_packages, setup


setup(
    name="clish",
    version="0.2",
    author="Vitold Sedyshev",
    author_email="vit1251@gmail.com",
    description="Command Line Interactive Shell Framework.",
    license="BSD",
    keywords="cli command line shell framework readline console",
    url="https://github.com/vit1251/clish",
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires=['apipkg'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
