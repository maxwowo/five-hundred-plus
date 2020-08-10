import pyfiglet


def pretty_print_title() -> None:
    pretty_print('Five Hundred Plus')


def pretty_print(text: str) -> None:
    print(pyfiglet.figlet_format(text))
