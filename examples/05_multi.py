from typing import Optional

from ty_cli import cli


@cli
def greet(*, first_name: str, last_name: Optional[str]) -> None:
    if last_name is None:
        print(f"Howdy {first_name}!")
    else:
        print(f"Greetings {first_name} {last_name}")


@cli
def bye(*, name: str) -> None:
    print(f"bye {name}!")


if __name__ == "__main__":
    cli()
