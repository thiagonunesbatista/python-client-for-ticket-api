import requests

from constants import ticketsResourceUrl

from helpers.auth import showFailedCredentialsMessage
from helpers.menu import goBackMenuMessage, showWrongMenuMessage


def showTicketsCrudMenu(authToken):
    while True:
        print("CRUD de Tickets")
        print("1. Criar")
        print("2. Listar")
        print("9. Voltar")

        selectedOption = int(input("Opção: "))
        print("\n")

        if selectedOption == 1:
            createTicket(authToken)

        elif selectedOption == 2:
            listTickets()

        elif selectedOption == 9:
            goBackMenuMessage()
            break

        else:
            showWrongMenuMessage()


def createTicket(authToken):
    print("Criação de ticket")

    if not authToken:
        showFailedCredentialsMessage()
        return


def listTickets():
    print("Listagem de Tickets")

    listTicketsResponse = requests.get(ticketsResourceUrl)

    if listTicketsResponse.status_code != 200:
        print("Erro... Não foi possível trazer os dados de tickets")
        return

    responseInJson = listTicketsResponse.json()

    if len(responseInJson) == 0:
        print("Não há tickets cadastrados\n")
        return

    for currentTicket in responseInJson:
        print(f"Nome: {currentTicket['eventName']}")
        print(f"Descrição: {currentTicket['description']}")
        print(f"Preço: R$ {currentTicket['price']}")
        print("\n")
