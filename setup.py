# SPDX-License-Identifier: GPL-2.0-only
#
# (C) Copyright IBM Corp. 2018, 2019
# Author: Sourabh Jain <sourabhjain@linux.ibm.com>

import os
import sys
from setuptools import setup, find_packages

from servicereportpkg import get_version

# Workaround for https://bugs.python.org/issue644744
if "bdist_rpm" in sys.argv[1:]:
    os.putenv("COMPRESS", " ")

setup(packages=find_packages(),
      scripts=['servicereport'],
      version=get_version(),
      data_files=[('share/man/man8', ['man/servicereport.8']),
                  ('share/doc/servicereport', ['README.md']),
                  ('/usr/lib/systemd/system', ['rpm/systemd/servicereport.service'])],
      options = {'bdist_rpm':{'post_install' : 'rpm/postscript'}},
      classifiers=[
          'Development Status :: 4 - Beta',
          'Programming Language :: Python'])
