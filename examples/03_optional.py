from typing import Optional

from ty_cli import cli


@cli
def greet(*, first_name: str, last_name: Optional[str]) -> None:
    if last_name is None:
        print(f"Howdy {first_name}!")
    else:
        print(f"Dear {first_name} {last_name}")
