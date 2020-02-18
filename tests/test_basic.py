import ty_cli


def _fun_int_to_str(number: int) -> str:
    """Some documentation"""
    return f"{number}"


def test_basic():
    wrapped_fun = ty_cli.cli(_fun_int_to_str)
    assert wrapped_fun(2) == "2"


def test_signature():  # Do we really want to do this?
    wrapped_fun = ty_cli.cli(_fun_int_to_str)
    assert wrapped_fun.__annotations__ == _fun_int_to_str.__annotations__
    assert wrapped_fun.__defaults__ == _fun_int_to_str.__defaults__
    assert wrapped_fun.__kwdefaults__ == _fun_int_to_str.__kwdefaults__


def test_create_argparse_from_function_signature():
    ty_cli.create_argparse_from_function_signature(_fun_int_to_str)
