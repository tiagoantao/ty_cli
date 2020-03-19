"""
    ty_cli
    ~~~~~~

    Easy command line interfaces in Python using explict typing.

    :copyright: Copyright 2019 - Tiago Antao.
    :license: AGPL 3.0, see LICENSE for details.
"""
import argparse
from collections import defaultdict
import copy
import inspect
import sys
import typing
from typing import Any, Callable, Dict, Optional, TypeVar, Union

F = Callable[..., Any]

module_calls: Dict[str, Dict[str, F]] = defaultdict(dict)


def create_argparse_from_function_signature(fun: F) -> argparse.ArgumentParser:
    """Creates argparse arguments from a function signature.

    :param fun: The function to extract the signature from.

    :returns: `argparse.ArgumentParser`. An ArgumentParser object.

    """
    parser = argparse.ArgumentParser(
        description=fun.__name__ + ": " + (fun.__doc__ or "NA")
    )
    arg_spec = inspect.getfullargspec(fun)
    for arg in arg_spec.args:
        annotations = arg_spec.annotations[arg]
        arg_cli = arg.replace("_", "-")
        if typing.get_origin(annotations) is Union and typing.get_args(annotations)[
            1
        ] is type(None):
            is_optional = True
            my_type = typing.get_args(annotations)[0]
        else:
            is_optional = False
            my_type = arg_spec.annotations[arg]
        has_default = arg_spec.defaults is not None and arg in arg_spec.defaults
        if is_optional or has_default:
            parser.add_argument(
                "--" + arg_cli,
                type=my_type,
                required=not is_optional,
                default=arg_spec.kwonlydefaults[arg]
                if arg_spec.kwonlydefaults is not None
                else None,
            )
        else:
            parser.add_argument(arg, type=arg_spec.annotations[arg])

    for arg in arg_spec.kwonlyargs:
        annotations = arg_spec.annotations[arg]
        arg_cli = arg.replace("_", "-")
        if typing.get_origin(annotations) is Union and typing.get_args(annotations)[
            1
        ] is type(None):
            is_optional = True
            my_type = typing.get_args(annotations)[0]
        else:
            is_optional = False
            my_type = arg_spec.annotations[arg]
        has_default = (
            arg_spec.kwonlydefaults is not None and arg in arg_spec.kwonlydefaults
        )
        if is_optional or has_default:
            parser.add_argument(
                "--" + arg_cli,
                type=my_type,
                default=arg_spec.kwonlydefaults[arg]
                if arg_spec.kwonlydefaults is not None
                else None,
            )
        else:
            parser.add_argument("--" + arg_cli, type=my_type, required=True)
    return parser


def call_with_arguments(fun: F, arguments: argparse.Namespace) -> None:
    fun(*arguments._get_args(), **dict(arguments._get_kwargs()))


def call_using_cli(fun: F) -> None:
    """Call a function parametrized by the CLI.

    :param fun: The function to extract the signature from.

    """
    parser = create_argparse_from_function_signature(fun)
    arguments = parser.parse_args()
    call_with_arguments(fun, arguments)


def cli(fun: Optional[F] = None) -> Optional[F]:
    """ This is the decorator AND invoker.

    If called with a function as a parameter, then its in decorator mode,
       marking a function for CLI parsing.
    If called with no parameters then its call to a decorated function and
       parameters will need to be fetched from the CLI before function
       execution.

    :param fun: The function to extract the signature from (Optional)

    :returns: If used as a decorator (has parameter) then return a function
    """
    # XXX Missing: it can be a direct call to the function!!!
    frame = inspect.currentframe()
    outer_frame = inspect.getouterframes(frame)[1]
    if fun is None:
        all_calls = module_calls[outer_frame.filename]
        if len(all_calls) == 0:
            pass
        elif len(all_calls) == 1:
            list(all_calls.values())[0]()
        else:
            subcommands = list(all_calls.keys())
            if len(sys.argv) < 2:
                print(
                    f"You need to specific a subcommand from: {subcommands}",
                    file=sys.stderr,
                )
                return None
            subcommand = sys.argv[1]
            if subcommand not in subcommands:
                print(
                    f"Your subcommand needs to be from {subcommands}", file=sys.stderr,
                )
                return None
            del sys.argv[1]
            all_calls[subcommand]()

        return None

    def wrapper(*args, **kwargs):  # type: ignore
        if len(args) > 0 or len(kwargs) > 0:
            # This is a non-cli call
            return fun(*args, **kwargs)  # type: ignore
        return call_using_cli(fun)  # type: ignore

    # Is this even a good idea:
    wrapper.__annotations__ = copy.copy(fun.__annotations__)
    wrapper.__defaults__ = copy.copy(fun.__defaults__)  # type: ignore
    wrapper.__kwdefaults__ = copy.copy(fun.__kwdefaults__)  # type: ignore
    # What about read-only fields like __code__.co.* ??
    module_calls[outer_frame.filename][fun.__name__] = wrapper
    return typing.cast(F, wrapper)


def _clean_call_dictionary():
    """Cleans the call dictionary"""
    module_calls = defaultdict


__all__ = ["__version__", "cli"]
__version__ = "0.0.1"
