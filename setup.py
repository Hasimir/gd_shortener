import codecs
from setuptools import setup

long_description = codecs.open('README.rst', "r").read()

setup(
    name = "gdshortener",
    version = "0.0.3",
    author = "Gian Luca Dalla Torre",
    author_email = "gianluca@gestionaleauto.com",
    description = ("A module that provides access to .gd URL Shortener"),
    license = "LGPL",
    keywords = "url shortener gd",
    url = "https://github.com/torre76/gd_shortener",
    download_url = "https://github.com/torre76/gd_shortener/releases",
    packages=['gdshortener'],
    long_description=long_description,
    package_data = {
        '': ['README.rst'],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Programming Language :: Python :: 2.7",
        # Will probably work with 3.2 and 3.3, but not tested.
        # "Programming Language :: Python :: 3.2",
        # "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3"
    ],
)
