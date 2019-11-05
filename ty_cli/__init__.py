"""
    ty_cli
    ~~~~~~

    Easy command line interfaces in Python using explict typing.

    :copyright: Copyright 2019- Tiago Antao.
    :license: AGPL 3.0, see LICENSE for details.
"""
import argparse
import copy
import inspect
from typing import Any, Callable, TypeVar, cast

__version__ = '0.0.1'

FuncType = Callable[..., Any]
F = TypeVar('F', bound=FuncType)


def create_argparse_from_function_signature(fun: F) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=fun.__name__)
    arg_spec = inspect.getfullargspec(fun)
    for arg in arg_spec.args:
        parser.add_argument(arg, type=arg_spec.annotations[arg])
        print(arg)
    for arg in arg_spec.kwonlyargs:
        if arg in (arg_spec.kwonlydefaults or {}):
            parser.add_argument('--' + arg, type=arg_spec.annotations[arg],
                                default=arg_spec.kwonlydefaults[arg])
        else:
            parser.add_argument('--' + arg, type=arg_spec.annotations[arg], required=True)
        print(arg)
    print(arg_spec, arg_spec.args, arg_spec.kwonlyargs)
    print(parser)
    return parser


def call_with_arguments(fun, arguments):
    pass


def try_call_using_cli(fun: F) -> None:
    parser = create_argparse_from_function_signature(fun)
    arguments = parser.parse_args()
    print(arguments)
    call_with_arguments(fun, arguments)


def emit_help(fun: F) -> str:
    pass


def cli(fun: F) -> F:
    def wrapper(*args, **kwargs):  # type: ignore
        if len(args) > 0 or len(kwargs) > 0:
            # This is a non-cli call
            return fun(*args, **kwargs)
        try_call_using_cli(fun)
    wrapper.__annotations__ = copy.copy(fun.__annotations__)
    wrapper.__defaults__ = copy.copy(fun.__defaults__)
    wrapper.__kwdefaults__ = copy.copy(fun.__kwdefaults__)
    # XXX What about read-only fields like __code__.co.* ??
    return cast(F, wrapper)


__all__ = ['__version__', 'cli']
