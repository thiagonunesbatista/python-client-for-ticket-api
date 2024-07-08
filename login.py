import requests

from constants import loginResourceUrl

from helpers.clean import clean
from helpers.menu import confirmBack


def makeLogin():
    clean()
    email = input("Digite seu Email: ")
    password = input("Digite sua senha: ")

    loginResponse = requests.post(
        loginResourceUrl, json={"email": email, "password": password}
    )

    if loginResponse.status_code != 200:
        print("Login ou Senha inválidos\n")
        confirmBack()
        return

    print("Login realizado com sucesso!\n")
    loginResponseInJson = loginResponse.json()
    confirmBack()

    return loginResponseInJson["token"]
