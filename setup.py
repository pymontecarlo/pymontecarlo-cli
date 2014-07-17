#!/usr/bin/env python

# Script information for the file.
__author__ = "Philippe T. Pinard"
__email__ = "philippe.pinard@gmail.com"
__version__ = "0.1"
__copyright__ = "Copyright (c) 2013 Philippe T. Pinard"
__license__ = "GPL v3"

# Standard library modules.
import os
import codecs
import re

# Third party modules.
from setuptools import setup, find_packages

# Local modules.
from pymontecarlo.util.dist.command.clean import clean
from pymontecarlo.util.dist.command.check import check

# Globals and constants variables.
BASEDIR = os.path.abspath(os.path.dirname(__file__))

def find_version(*file_paths):
    """
    Read the version number from a source file.

    .. note::

       Why read it, and not import?
       see https://groups.google.com/d/topic/pypa-dev/0PkjVpcxTzQ/discussion
    """
    # Open in Latin-1 so that we avoid encoding errors.
    # Use codecs.open for Python 2 compatibility
    with codecs.open(os.path.join(BASEDIR, *file_paths), 'r', 'latin1') as f:
        version_file = f.read()

    # The version line must have the form
    # __version__ = 'ver'
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

packages = find_packages(exclude=('pymontecarlo.util.dist*',))
namespace_packages = ['pymontecarlo',
                      'pymontecarlo.ui']
requirements = ['pymontecarlo', 'pyxray']

cli_executables = {'pymontecarlo-configure': 'pymontecarlo.ui.cli.configure:run',
                   'pymontecarlo-cli': 'pymontecarlo.ui.cli.main:run',
                   'pymontecarlo-updater': 'pymontecarlo.ui.cli.updater:run'}

entry_points = {}
entry_points['console_scripts'] = \
    ['%s = %s' % item for item in cli_executables.items()]

setup(name="pyMonteCarlo-CLI",
      version=find_version('pymontecarlo', '__init__.py'),
      url='http://pymontecarlo.bitbucket.org',
      description="Python interface for Monte Carlo simulation programs",
      author="Hendrix Demers and Philippe T. Pinard",
      author_email="hendrix.demers@mail.mcgill.ca and philippe.pinard@gmail.com",
      license="GPL v3",
      classifiers=['Development Status :: 4 - Beta',
                   'Intended Audience :: End Users/Desktop',
                   'License :: OSI Approved :: GNU General Public License (GPL)',
                   'Natural Language :: English',
                   'Programming Language :: Python',
                   'Operating System :: OS Independent',
                   'Topic :: Scientific/Engineering',
                   'Topic :: Scientific/Engineering :: Physics'],

      packages=packages,
      namespace_packages=namespace_packages,

      cmdclass={'clean': clean, "check": check},

      setup_requires=['nose'],
      install_requires=requirements,

      entry_points=entry_points,

      test_suite='nose.collector',
)

