import sys
from typing import Optional

import ty_cli


def _fun_int_to_str_opt(number: Optional[int]) -> str:
    """Some documentation"""
    if number is None:
        return "???"
    else:
        return f"{number}"


def _fun_add_int_to_str(number1: int, number2: int = 0) -> str:
    """Integer sum to String"""
    return f"{number1 + number2}"


def test_optional():
    """Tests optional call"""
    wrapped_fun = ty_cli.cli(_fun_int_to_str_opt)
    assert wrapped_fun(2) == "2"
    assert wrapped_fun(None) == "???"


def test_main_invocation():
    """Testing cli without a function (as from __main__).
    """
    sys.argv = ['TEST', '--number', '5']
    # Optional example
    ty_cli._clean_call_dictionary()
    ty_cli.cli(_fun_int_to_str_opt)
    ty_cli.cli()
    # default example
    #ty_cli._clean_call_dictionary()
    #ty_cli.cli(_fun_add_int_to_str)
    #ty_cli.cli()
