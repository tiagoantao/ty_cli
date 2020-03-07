# ty_cli

[![Build Status](https://dev.azure.com/tiagoantao/ty_cli/_apis/build/status/tiagoantao.ty_cli?branchName=master)](https://dev.azure.com/tiagoantao/ty_cli/_build/latest?definitionId=2&branchName=master)
[![Code style: black](https://pepy.tech/badge/black)](https://pepy.tech/badge/black)

## Intro

ty_cli is an extremely opinionated command line parsing
library. Because it decides everything for you, its interface is dead
simple. Its particularly good if you need a quick CLI interface with
almost zero effort.

It is based on and requires type annotations (à la mypy). Uses Python
3.7 or above.


## Examples

### Hello world

```python
from ty_cli import cli

@cli
def hello(name: str) -> None:
    '''Hello world: the typical example.
    
    Here is some documentation'''
    print(f'Hello {name}')
    
hello()
```

`python hello.py --help`

`python hello.py Randi`

If you want, you can force the naming on parameters on the CLI:

```python
from ty_cli import cli

@cli
def hello(*, name: str) -> None:
    print(f'Hello {name}')
```

`python hello.py --name Randi`


[Documentation](docs/index.rst)


## Legalese

Copyright 2019- Tiago Rodrigues Antao.

Licensed under the GNU Affero General Public License version 3.

