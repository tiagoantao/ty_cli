from ty_cli import cli


@cli
def greet(*, first_name: str, last_name: str = "Smith") -> None:
    if last_name is None:
        print(f"Howdy {first_name}!")
    else:
        print(f"Dear {first_name} {last_name}")


if __name__ == "__main__":
    cli()
