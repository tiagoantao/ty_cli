from ty_cli import cli


@cli
def int_to_str(number: int) -> str:
    return f"{number}"


if __name__ == "__main__":
    int_to_str()
    # Alernatively you can do cli()
