from helpers.menu import goBackMenuMessage, showWrongMenuMessage


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
        elif selectedOption == 1:
            listUsers()
        elif selectedOption == 3:
            goBackMenuMessage()
            break
        else:
            showWrongMenuMessage()


def createUser():
    print("Create User")


def listUsers():
    print("List Users")
