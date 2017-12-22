#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.me') as readme_file:
    readme = readme_file.read()

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    'pytest'
    # TODO: put package test requirements here
]

setup(
    name='tyt_download_automator',
    version='0.0.0',
    description="TYT Download Automator automates the process of downloading new episodes for members of the TYT Network",
    long_description=readme + '\n\n',
    author="Zach Mitchell",
    author_email='zmitchell@fastmail.com',
    url='https://github.com/zmitchell/tyt_download_automator',
    packages=find_packages(),
    package_dir={'tyt_download_automator':
                 'tyt_download_automator'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='tyt_download_automator',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6'
    ],
    test_suite='tests',
    tests_require=test_requirements,
    entry_points={
        'console_scripts': [
            'tyt_download_automator = tyt_download_automator.__main__:main'
        ]
    }
)
