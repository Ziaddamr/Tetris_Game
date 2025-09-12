import os


def clear():
    if os.name == 'nt':
        os.system('cls')


def hide_cursor():
    print("\033[?25l", end="")


def show_cursor():
    print("\033[?25h", end="")
