#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_version(*file_paths):
    """Retrieves the version from dj_jb_zerodowntime/__init__.py"""
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


version = get_version("dj_jb_zerodowntime", "__init__.py")


if sys.argv[-1] == "publish":
    try:
        import wheel

        print("Wheel version: ", wheel.__version__)
    except ImportError:
        print('Wheel library missing. Please run "pip install wheel"')
        sys.exit()
    os.system("python setup.py sdist upload")
    os.system("python setup.py bdist_wheel upload")
    sys.exit()

if sys.argv[-1] == "tag":
    print("Tagging the version on git:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

readme = open("README.rst").read()
history = open("HISTORY.rst").read().replace(".. :changelog:", "")
# requirements = open('requirements.txt').readlines()

setup(
    name="dj-jb-zerodowntime",
    version=version,
    description="""Management commands to help Django users build & deploy their projects with low interruption for their users. This method is often called Zero Downtime Continous Delivery, or ZDCD.""",
    long_description=readme + "\n\n" + history,
    author="Jake Berkson",
    author_email="test@test.invalid",
    url="https://github.com/berksonj/dj-jb-zerodowntime",
    packages=[
        "dj_jb_zerodowntime",
    ],
    include_package_data=True,
    # install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords="dj-jb-zerodowntime",
    classifiers=[
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.8",
    ],
)
