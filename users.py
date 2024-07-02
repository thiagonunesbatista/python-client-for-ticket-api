import requests

from constants import baseUrl, userResourceUrl

from helpers.menu import goBackMenuMessage, showWrongMenuMessage


usersResourceFullUrl = baseUrl + userResourceUrl


def showUsersCrudMenu():

    while True:
        print("CRUD de usuários")
        print("1. Criar")
        print("2. Listar")
        print("3. Voltar")

        selectedOption = int(input("Opção: "))
        print("\n")

        if selectedOption == 1:
            createUser()
        elif selectedOption == 2:
            listUsers()
        elif selectedOption == 3:
            goBackMenuMessage()
            break
        else:
            showWrongMenuMessage()


def createUser():
    print("Create User")


def listUsers():
    print("Listagem de Usuários")

    listUsersResponse = requests.get(usersResourceFullUrl)

    if listUsersResponse.status_code != 200:
        print("Erro... Não foi possível trazer os dados de usuários")
        return

    responseInJson = listUsersResponse.json()

    if(len(responseInJson) == 0):
        print("Não há usuários cadastrados")
        return

    for currentUser in responseInJson:
        print(f"Nome: {currentUser['name']}")
        print(f"Email: {currentUser['email']}")
        print("\n")
