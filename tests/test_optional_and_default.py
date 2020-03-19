from typing import Optional

import ty_cli


def _fun_int_to_str_opt(number: Optional[int]) -> str:
    """Some documentation"""
    if number is None:
        return "???"
    else:
        return f"{number}"


def test_optional():
    """Tests optionals"""
    wrapped_fun = ty_cli.cli(_fun_int_to_str_opt)
    assert wrapped_fun(2) == "2"
    assert wrapped_fun(None) == "???"
