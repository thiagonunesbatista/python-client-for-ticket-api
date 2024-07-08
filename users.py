import requests

from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from constants import userResourceUrl

from helpers.auth import showFailedCredentialsMessage
from helpers.menu import goBackMenuMessage, showWrongMenuMessage
from helpers.clean import clean


def showUsersDataMenu(authToken):

    while True:
        clean()
        selectMenu = inquirer.select(
            message="Dados de usuários:",
            choices=[
                Choice(value=1, name="Criar"),
                Choice(value=2, name="Listar"),
                Choice(value=3, name="Voltar"),
            ],
            default=None,
        ).execute()

        if selectMenu == 1:
            createUser(authToken)
        elif selectMenu == 2:
            listUsers()
        elif selectMenu == 3:
            goBackMenuMessage()
            break
        else:
            showWrongMenuMessage()


def createUser(authToken):
    print("Criação de usuário")

    if not authToken:
        showFailedCredentialsMessage()
        return

    print("Digite os dados do usuário:")

    userName = input("Nome: ")
    userEmail = input("Email: ")
    userPassword = input("Senha: ")

    headderTokenAuth = {"Authorization": "Bearer " + authToken}

    createUserResponse = requests.post(
        userResourceUrl,
        json={"email": userEmail, "password": userPassword, "name": userName},
        headers=headderTokenAuth,
    )
    if createUserResponse.status_code != 201:
        print("Erro interno ao tentar criar usuário")
        return

    print("\nUsuário criado com sucesso\n")


def listUsers():
    print("Listagem de Usuários")

    listUsersResponse = requests.get(userResourceUrl)

    if listUsersResponse.status_code != 200:
        print("Erro... Não foi possível trazer os dados de usuários")
        return

    responseInJson = listUsersResponse.json()

    if len(responseInJson) == 0:
        print("Não há usuários cadastrados\n")
        return

    for currentUser in responseInJson:
        print(f"Nome: {currentUser['name']}")
        print(f"Email: {currentUser['email']}")
        print("\n")
