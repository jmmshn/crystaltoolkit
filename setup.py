# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = ""

setup(
    long_description=readme,
    name="crystal_toolkit",
    version="2020.06.04",
    python_requires="==3.*,>=3.7.0",
    author="Matthew Horton",
    author_email="mkhorton@lbl.gov",
    packages=[
        "crystal_toolkit",
        "crystal_toolkit.apps",
        "crystal_toolkit.apps.examples",
        "crystal_toolkit.apps.examples.tests",
        "crystal_toolkit.apps.tests",
        "crystal_toolkit.components",
        "crystal_toolkit.components.transformations",
        "crystal_toolkit.core",
        "crystal_toolkit.core.tests",
        "crystal_toolkit.helpers",
        "crystal_toolkit.renderables",
    ],
    package_data={
        "crystal_toolkit": ["*.json"],
        "crystal_toolkit.apps": ["assets/*.ico", "assets/*.json", "assets/*.png"],
        "crystal_toolkit.apps.examples": ["*.json"],
        "crystal_toolkit.core": ["*.yaml"],
    },
    install_requires=[],
    extras_require={"dev": []},
)
