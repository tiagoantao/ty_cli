"""
    ty_cli
    ~~~~~~

    Easy command line interfaces in Python using explict typing.

    :copyright: Copyright 2019- Tiago Antao.
    :license: AGPL 3.0, see LICENSE for details.
"""
from typing import Any, Callable, TypeVar, cast


__version__ = '0.0.1'


FuncType = Callable[..., Any]
F = TypeVar('F', bound=FuncType)


def cli(fun: F) -> F:
    def wrapper(*args, **kwargs):  # type: ignore
        return fun(*args, **kwargs)
    return cast(F, wrapper)


@cli
def bla(a: int, b: str) -> None:
    pass

__all__ = ['__version__', 'cli']
