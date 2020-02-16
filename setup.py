import re
from setuptools import setup

with open('src/ty_cli/__init__.py', 'rt', encoding='utf8') as f:
    version = re.search(r"__version__ = '(.*?)'", f.read()).group(1)

extras_require = {
    'test': [
        'mypy>=0.740',
        'pytest',
        'pytest-cov',
        'tox'
    ],
    'docs': [
        'sphinx',
        'sphinx-rtd-theme',
    ],
}

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU Affero General Public License v3',
    'Topic :: Software Development :: Libraries'
]

setup(name='ty_cli',
      version=version,
      description='Easy command line interfaces in Python based on explict typing',
      url='http://github.com/tiagoantao/ty_cli',
      author='Tiago Antao',
      author_email='tiago@tiago.org',
      license='AGPLv3',
      python_requires=">=3.7",
      classifiers=CLASSIFIERS
      )
