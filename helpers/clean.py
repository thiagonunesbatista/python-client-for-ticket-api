import os


def clean():
    if os.name == "nt":
        _ = os.system("cls")

    else:
        _ = os.system("clear")
