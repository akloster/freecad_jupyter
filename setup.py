#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
===============================
HtmlTestRunner
===============================


.. image:: https://img.shields.io/pypi/v/freecad_jupyter.svg
        :target: https://pypi.python.org/pypi/freecad_jupyter
.. image:: https://img.shields.io/travis/akloster/freecad_jupyter.svg
        :target: https://travis-ci.org/akloster/freecad_jupyter

A Kernel and Utilities to control FreeCAD from Jupyter Notebook and Lab


Links:
---------
* `Github <https://github.com/akloster/freecad_jupyter>`_
"""

from setuptools import setup, find_packages

requirements = [ ]

setup_requirements = ["notebook", "ipython","pyside2"]

test_requirements = [ ]

setup(
    author="Andreas Klostermann",
    author_email='andreasklostermann@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    description="A Kernel and Utilities to control FreeCAD from Jupyter Notebook and Lab",
    install_requires=requirements,
    license="MIT license",
    long_description=__doc__,
    include_package_data=True,
    keywords='freecad_jupyter',
    name='freecad_jupyter',
    packages=find_packages(include=['freecad_jupyter']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/akloster/freecad_jupyter',
    version='0.1.0',
    zip_safe=False,
)
