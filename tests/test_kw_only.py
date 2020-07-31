import sys
from typing import Optional

import ty_cli


def _fun_int_to_str_kw(*, number: int) -> str:
    """Parameter has to be named"""
    return f"{number}"


def _fun_int_to_str_kw_optional(*, number: Optional[int] = None) -> str:
    """Parameter has to be named"""
    if number is None:
        return "Nothing here"
    else:
        return f"{number}"


def _fun_add_int_to_str_kw(*, number1: int, number2: int = 0) -> str:
    """Integer sum to String"""
    return f"{number1 + number2}"


def test_kwonly():
    """Tests keyowrd only call"""
    ty_cli._clean_call_dictionary()
    wrapped_fun = ty_cli.cli(_fun_add_int_to_str_kw)
    assert wrapped_fun(number1=2) == "2"


def test_kwonly_optional():
    """Tests keyowrd only call"""
    ty_cli._clean_call_dictionary()
    wrapped_fun = ty_cli.cli(_fun_int_to_str_kw_optional)
    assert wrapped_fun(number=None) == "Nothing here"


def test_main_invocation():
    """Testing cli without a function (as from __main__).
    """
    sys.argv = ["TEST", "--number1", "5"]
    # Optional example
    ty_cli._clean_call_dictionary()
    ty_cli.cli(_fun_add_int_to_str_kw)
    ty_cli.cli()
    ty_cli._clean_call_dictionary()
    sys.argv = ['TEST']
    ty_cli.cli(_fun_int_to_str_kw_optional)
    ty_cli.cli()
