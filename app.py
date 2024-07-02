from users import showUsersCrudMenu


def startMenu():
    def showWrongMenuMessage():
        print("Esta opção não existe, tente novamente !!!")

    def exitApp():
        print("Saindo do APP...")

    while True:
        print("Integração de Python com API de Tickets")
        print("1. CRUD de Usuários")
        print("9. Sair")

        selectedOption = int(input("Opção: "))
        print("\n")

        if selectedOption == 1:
            showUsersCrudMenu()
        elif selectedOption == 9:
            exitApp()
            break
        else:
            showWrongMenuMessage()


startMenu()
