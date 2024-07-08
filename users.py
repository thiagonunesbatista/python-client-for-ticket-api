import requests

from constants import userResourceUrl

from helpers.auth import showFailedCredentialsMessage
from helpers.menu import goBackMenuMessage, showWrongMenuMessage


def showUsersDataMenu(authToken):

    while True:
        print("Dados de usuários")
        print("1. Criar")
        print("2. Listar")
        print("3. Voltar")

        selectedOption = int(input("Opção: "))
        print("\n")

        if selectedOption == 1:
            createUser(authToken)
        elif selectedOption == 2:
            listUsers()
        elif selectedOption == 3:
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
