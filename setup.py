#!/usr/bin/python
from setuptools import setup, find_packages

# Import the module version
from netapp_ocum import __version__

# Run the setup
setup(
    name             = 'netapp_ocum',
    version          = __version__,
    description      = 'Client bindings for for the NetApp OnCommand Unified Manager (OCUM) REST API.',
    long_description = open('DESCRIPTION.rst').read(),
    author           = 'David Taylor',
    author_email     = 'djtaylor13@gmail.com',
    url              = 'http://github.com/djtaylor/python-netapp-ocum',
    license          = 'GPLv3',
    test_suite       = 'nose.collector',
    tests_require    = ['nose'],
    packages         = find_packages(),
    keywords         = 'netapp nfs api http ocum',
    classifiers      = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Terminals',
    ]
)
