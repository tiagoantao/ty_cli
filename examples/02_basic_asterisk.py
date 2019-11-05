from ty_cli import cli


@cli
def int_to_str(*, number: int, my_str: str = 'abc') -> str:
    return f'{number} {my_str}'


int_to_str()
