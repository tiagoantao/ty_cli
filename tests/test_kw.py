import sys

import ty_cli


def _fun_int_to_str_kw(*, number: int) -> str:
    """Parameter has to be named"""
    return f"{number}"


def _fun_add_int_to_str_kw(*, number1: int, number2: int = 0) -> str:
    """Integer sum to String"""
    return f"{number1 + number2}"


def test_kwargs():
    """Tests kwarg call"""
    wrapped_fun = ty_cli.cli(_fun_int_to_str_kw)
    assert wrapped_fun(number=2) == "2"


def test_main_invocation():
    """Testing cli without a function (as from __main__).
    """
    sys.argv = ['TEST', '--number1', '5']
    # Optional example
    ty_cli._clean_call_dictionary()
    ty_cli.cli(_fun_add_int_to_str_kw)
    ty_cli.cli()

