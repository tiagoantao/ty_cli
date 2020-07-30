import re
from setuptools import find_packages, setup

with open("src/ty_cli/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r"__version__ = \"(.*?)\"", f.read()).group(1)

EXTRAS_REQUIRE = {
    "test": ["mypy>=0.740", "pytest", "pytest-cov", "tox"],
    "docs": ["sphinx", "sphinx-rtd-theme",],
}

CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: GNU Affero General Public License v3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3 :: Only",
    "Topic :: Software Development :: Libraries",
]

setup(
    name="ty_cli",
    version=version,
    description="Easy command line interfaces in Python based on explict typing",
    url="http://github.com/tiagoantao/ty_cli",
    author="Tiago Antao",
    author_email="tiago@tiago.org",
    license="AGPLv3",
    packages=find_packages("src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    extras_require=EXTRAS_REQUIRE,
    classifiers=CLASSIFIERS,
)
