#!/usr/bin/env python

from os import walk
from os.path import join, relpath

from setuptools import setup


version = "4.2.0"

requires = [
    "feedgenerator >= 1.9",
    "jinja2 >= 2.11",
    "pygments",
    "docutils>=0.15",
    "pytz >= 0a",
    "blinker",
    "unidecode",
    "python-dateutil",
]

entry_points = {
    "console_scripts": [
        "pelican = pelican.__main__:main",
        "pelican-import = pelican.tools.pelican_import:main",
        "pelican-quickstart = pelican.tools.pelican_quickstart:main",
        "pelican-themes = pelican.tools.pelican_themes:main",
        "pelican-plugins = pelican.plugins._utils:list_plugins",
    ]
}

README = open("README.rst", encoding="utf-8").read()
CHANGELOG = open("docs/changelog.rst", encoding="utf-8").read()

description = "\n".join([README, CHANGELOG])

setup(
    name="pelican",
    version="4.0.2.dev0-crossjam",
    url="https://getpelican.com/",
    author="Justin Mayer",
    author_email="authors@getpelican.com",
    description="Static site generator supporting reStructuredText and "
    "Markdown source content.",
    project_urls={
        "Documentation": "https://docs.getpelican.com/",
        "Funding": "https://donate.getpelican.com/",
        "Source": "https://github.com/getpelican/pelican",
        "Tracker": "https://github.com/getpelican/pelican/issues",
    },
    keywords="static web site generator SSG reStructuredText Markdown",
    license="AGPLv3",
    long_description=description,
    packages=["pelican", "pelican.tools", "pelican.plugins"],
    package_data={
        # we manually collect the package data, as opposed to using,
        # include_package_data=True because we don't want the tests to be
        # included automatically as package data (MANIFEST.in is too greedy)
        "pelican": [
            relpath(join(root, name), "pelican")
            for root, _, names in walk(join("pelican", "themes"))
            for name in names
        ],
        "pelican.tools": [
            relpath(join(root, name), join("pelican", "tools"))
            for root, _, names in walk(join("pelican", "tools", "templates"))
            for name in names
        ],
    },
    install_requires=requires,
    extras_require={"Markdown": ["markdown~=3.1.1"]},
    entry_points=entry_points,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Framework :: Pelican",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    test_suite="pelican.tests",
)
