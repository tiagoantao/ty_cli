import sys
from typing import Optional

import ty_cli


def _fun_int_to_str(number: int) -> str:
    """Integer to String"""
    return f"{number}"


def _fun_int_to_str_opt(number: Optional[int]) -> str:
    """Integer (or None) to String"""
    if number is None:
        return "Nothing"
    else:
        return f"{number}"


def _fun_add_int_to_str(number1: int, number2: int = 0) -> str:
    """Integer sum to String"""
    return f"{number1 + number2}"


def test_basic():
    """Tests if a wrapped function, returns the expected value"""
    wrapped_fun = ty_cli.cli(_fun_int_to_str)
    assert wrapped_fun(2) == "2"


def test_signature():  # Do we really want to do this?
    """Test function signature"""
    wrapped_fun = ty_cli.cli(_fun_int_to_str)
    assert wrapped_fun.__annotations__ == _fun_int_to_str.__annotations__
    assert wrapped_fun.__defaults__ == _fun_int_to_str.__defaults__
    assert wrapped_fun.__kwdefaults__ == _fun_int_to_str.__kwdefaults__


def test_main_invocation():
    """Testing cli without a function parameter (as from __main__).
    """
    sys.argv = ["TEST", "5"]
    ty_cli._clean_call_dictionary()
    ty_cli.cli(_fun_int_to_str)
    ty_cli.cli()


def test_subcommands():
    """Testing cli without a function (as from __main__). Subcommand version.
    """
    # XXX Need to grab output
    sys.argv = ["TEST", "_fun_int_to_str", "3"]
    ty_cli._clean_call_dictionary()
    ty_cli.cli(_fun_int_to_str)
    ty_cli.cli(_fun_add_int_to_str)
    ty_cli.cli()
    sys.argv = ["TEST"]
    ty_cli.cli()
    sys.argv = ["TEST", "5"]
    ty_cli.cli()


# def test_create_argparse_from_function_signature():
#     ty_cli.create_argparse_from_function_signature(_fun_int_to_str)


def test_sillyness():
    # Just to make coverage of the test file go to 100%
    _fun_add_int_to_str(1, 2)
    _fun_int_to_str_opt(None)
    _fun_int_to_str_opt(1)
