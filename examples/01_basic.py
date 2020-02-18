from ty_cli import cli


@cli
def int_to_str(number: int) -> str:
    return f"{number}"


int_to_str()
