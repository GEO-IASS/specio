import os
from setuptools import setup, find_packages

# get __version__ from _version.py
ver_file = os.path.join('specio', '_version.py')
with open(ver_file) as f:
    exec(f.read())

PACKAGES = find_packages()

CLASSIFIERS = ["Environment :: Console",
               "Intended Audience :: Science/Research",
               "License :: OSI Approved :: BSD 3",
               "Operating System :: OS Independent",
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3.4',
               'Programming Language :: Python :: 3.5',
               'Programming Language :: Python :: 3.6',
               "Topic :: Scientific/Engineering"]

description = "specio: Python input/output for spectroscopic files."
# Long description will go up on the pypi page
long_description = """

specio
======
Python input/output for spectroscopic files.
"""

NAME = "specio"
MAINTAINER = "Guillaume Lemaitre"
MAINTAINER_EMAIL = "glemaitre58@gmail.com"
DESCRIPTION = description
LONG_DESCRIPTION = long_description
URL = "https://github.com/paris-saclay-cds/specio"
DOWNLOAD_URL = ""
LICENSE = "BSD3"
AUTHOR = "Guillaume Lemaitre"
AUTHOR_EMAIL = "g.lemaitre58@gmail.com"
PLATFORMS = "OS Independent"
VERSION = __version__
PACKAGE_DATA = {'specio': ['core/tests/data/*.*',
                           'plugins/tests/data/*.*',
                           'datasets/data/*.*']}
EXTRAS_REQUIRE = {
    'tests': [
        'pytest',
        'pytest-cov'],
    'docs': [
        'sphinx',
        'sphinx-gallery',
        'sphinx_rtd_theme',
        'numpydoc',
        'matplotlib',
    ]
}

opts = dict(name=NAME,
            maintainer=MAINTAINER,
            maintainer_email=MAINTAINER_EMAIL,
            description=DESCRIPTION,
            long_description=LONG_DESCRIPTION,
            url=URL,
            download_url=DOWNLOAD_URL,
            license=LICENSE,
            classifiers=CLASSIFIERS,
            author=AUTHOR,
            author_email=AUTHOR_EMAIL,
            platforms=PLATFORMS,
            version=VERSION,
            packages=PACKAGES,
            package_data=PACKAGE_DATA,
            include_package_data=True,
            extras_require=EXTRAS_REQUIRE)


if __name__ == '__main__':
    setup(**opts)
