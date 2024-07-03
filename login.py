import requests

from constants import loginResourceUrl


def makeLogin():
    email = input("Digite seu Email: ")
    password = input("Digite sua senha: ")

    loginResponse = requests.post(
        loginResourceUrl, json={"email": email, "password": password}
    )

    if loginResponse.status_code != 200:
        print("Login ou Senha inválidos")
        print("\n")
        return

    print("Login realizado com sucesso!")
    print("\n")
    loginResponseInJson = loginResponse.json()

    return loginResponseInJson["token"]