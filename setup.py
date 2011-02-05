#!/usr/bin/env python
from distutils.core import setup
from html_blocks import VERSION
path='html_blocks'

setup(name=path,
      version=VERSION,
      description='html blocks for django templates',
      long_description = open('README.txt').read(),
      author='NORD',
      author_email='nordmenss@gmail.com',
      url='https://github.com/nordmenss/django-html-blocks',
      packages=[ path, 'html_blocks.templatetags',],

      classifiers=(
          'Development Status :: 2 - Pre-Alpha',
          'Environment :: Console',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Operating System :: POSIX',
          'Operating System :: Unix',
          'Programming Language :: Python',
        ),
      license="GPL"
     )