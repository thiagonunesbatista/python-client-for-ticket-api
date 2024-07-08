from login import makeLogin
from tickets import showTicketsCrudMenu
from users import showUsersDataMenu
from moreInformations import showMoreInformationMenu

from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from helpers.menu import exitApp, showWrongMenuMessage
from helpers.clean import clean


def startMenu():
    authToken = ""

    while True:
        clean()
        selectMenu = inquirer.select(
            message="Integração de Python com API de Tickets: ",
            choices=[
                Choice(value=1, name="Dados de Usuários"),
                Choice(value=2, name="Dados dos Tickets"),
                Choice(value=3, name="Informações Adicionais"),
                Choice(value=4, name="Fazer Login"),
                Choice(value=5, name="Sair"),
            ],
            default=None,
        ).execute()

        if selectMenu == 1:
            showUsersDataMenu(authToken)

        elif selectMenu == 2:
            showTicketsCrudMenu(authToken)

        elif selectMenu == 3:
            showMoreInformationMenu()

        elif selectMenu == 4:
            loginToken = makeLogin()

            if loginToken:
                authToken = loginToken

        elif selectMenu == 5:
            exitApp()
            break
        else:
            showWrongMenuMessage()


startMenu()
