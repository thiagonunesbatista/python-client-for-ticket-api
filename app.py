from login import makeLogin
from users import showUsersCrudMenu

from helpers.menu import exitApp, showWrongMenuMessage


def startMenu():
    authToken = ""

    while True:
        print("Integração de Python com API de Tickets")
        print("1. Dados de Usuários")
        print("3. Fazer Login")
        print("9. Sair")

        selectedOption = int(input("Opção: "))
        print("\n")

        if selectedOption == 1:
            showUsersCrudMenu(authToken)

        elif selectedOption == 3:
            loginToken = makeLogin()

            if loginToken:
                authToken = loginToken

        elif selectedOption == 9:
            exitApp()
            break
        else:
            showWrongMenuMessage()


startMenu()
