import codecs
from setuptools import setup

long_description = codecs.open('README.rst', "r").read()

setup(
    name = "gdshortener",
    version = "0.0.3",
    author = "Ben McGinnes",
    author_email = "ben@adversary.org"
    description = ("A module that provides access to is.gd and v.gd URL Shorteners"),
    license = "LGPL",
    keywords = "url shortener gd",
    url = "https://github.com/Hasimir/gd_shortener",
    download_url = "https://github.com/Hasimir/gd_shortener/tree/2to3/python3",
    packages=['gdshortener'],
    long_description=long_description,
    package_data = {
        '': ['README.rst'],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3 :: Only"
    ],
)
