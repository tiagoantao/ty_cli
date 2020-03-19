# ty_cli

[![Build Status](https://dev.azure.com/tiagoantao/ty_cli/_apis/build/status/tiagoantao.ty_cli?branchName=master)](https://dev.azure.com/tiagoantao/ty_cli/_build/latest?definitionId=2&branchName=master)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Intro

ty_cli is an extremely opinionated command line parsing
library. Because it decides everything for you, its interface is dead
simple. Its particularly good if you need a quick CLI interface with
almost zero effort.

It is based on and requires type annotations (à la mypy). Uses Python
3.8 or above.


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

### Named parameters

If you want, you can force the naming on parameters on the CLI
(exactly as you would force it in Python, of course):

```python
from ty_cli import cli

@cli
def hello(*, name: str) -> None:
    print(f'Hello {name}')
```

`python hello.py --name Randi`


### Multiple commands

ty_cli supports multiple commands:


```python
from typing import Optional

from ty_cli import cli


@cli
def greet(*, first_name: str, last_name: Optional[str]) -> None:
    if last_name is None:
        print(f"Howdy {first_name}!")
    else:
        print(f"Greetings {first_name} {last_name}")


@cli
def bye(*, name: str) -> None:
    print(f"Bye {name}!")


if __name__ == "__main__":
    cli()
```

This can be used as follows:

```sh
python multi_hello.py greet --first-name Randi
Howdy Randi!

python multi_hello.py greet --first-name Randi --last-name Taira
Greetings Randi Taira

python multi_hello.py bye --name Randi
Bye Randi!
```


## Documentation

[Documentation is available with more examples](docs/index.rst)


## Legalese

Copyright 2019- Tiago Rodrigues Antao.

Licensed under the GNU Affero General Public License version 3.

