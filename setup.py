import os
from setuptools import Command, find_packages, setup

import ty_cli


class Sphinx(Command):
    user_options = []
    description = 'build sphinx documentation'

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        # metadata contains information supplied in setup()
        metadata = self.distribution.metadata
        src_dir = os.path.join(os.getcwd(),  'ty_cli')
        # Run sphinx by calling the main method, '--full' also adds a conf.py
        from sphinx.ext import apidoc
        apidoc.main(
            ['-f', '-o', os.path.join('docs', 'api'), src_dir])
        # build the doc sources
        os.system('make html')


setup(name='ty_cli',
      version=ty_cli.__version__,
      description='Easy command line interfaces in Python based on explict typing',
      url='http://github.com/tiagoantao/ty_cli',
      author='Tiago Antao',
      author_email='tiagoantao@gmail.com',
      license='AGPLv3',
      packages=find_packages(),
      python_requires=">=3.6",
      cmdclass={ 'doc': Sphinx },
      )
