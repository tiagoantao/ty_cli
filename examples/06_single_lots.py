from typing import Optional

from ty_cli import cli


@cli
def hello_complex(name: str, *, birth_place: str, age: Optional[int] = None) -> None:
    print(f"Hello {name}, you were born in {birth_place}")
    if age:
        print(f"You are {age} years old")


if __name__ == "__main__":
    hello_complex()
