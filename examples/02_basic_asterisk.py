from ty_cli import cli


@cli
def int_to_str(*, number: int, my_str: str = 'abc') -> str:
    '''This is some documentation:

    Here is more'''
    my_str = f'{number} {my_str}'
    print(my_str)
    return my_str


cli()
