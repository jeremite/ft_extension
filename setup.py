#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
setup file
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="v_ft", # Replace with your own username
    version="0.0.12",
    author="Travis_li",
    author_email="wli10@email.wm.edu",
    description="featuretools related extensions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jeremite/ft_extension",
    packages=setuptools.find_packages(include=['v_ft','v_ft.*']),
    package_data = {
            'v_ft':['data/*.json']},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)