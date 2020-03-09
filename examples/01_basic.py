from ty_cli import cli


@cli
def int_to_str(number: int) -> str:
    return f"{number}"


# This is not the best practice to invoke it, but serves to demonstrate
# that the function signature is altered via the decorator.
# See the 02_ example for the typical way to invoke cli
int_to_str()
