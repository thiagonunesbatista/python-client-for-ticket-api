from InquirerPy import inquirer


def goBackMenuMessage():
    print("Retornando ao menu anterior...\n")


def showWrongMenuMessage():
    print("Esta opção não existe, tente novamente !!!\n")


def exitApp():
    print("Saindo do APP...\n")


def confirmBack():
    inquirer.confirm(message="Voltar?", default=True).execute()
