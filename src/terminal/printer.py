import pyfiglet


def pretty_print_title() -> None:
    pretty_print('Five Hundred Plus', justify='center')


def pretty_print(text: str, **kwargs) -> None:
    print(pyfiglet.figlet_format(text, **kwargs))
