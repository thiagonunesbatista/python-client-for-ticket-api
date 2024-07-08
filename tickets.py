import requests

from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from constants import ticketsResourceUrl

from helpers.auth import showFailedCredentialsMessage
from helpers.menu import goBackMenuMessage, showWrongMenuMessage


def showTicketsCrudMenu(authToken):
    while True:
        print("CRUD de Tickets")
        print("1. Criar")
        print("2. Listar")
        print("3. Deletar")
        print("9. Voltar")

        selectedOption = int(input("Opção: "))
        print("\n")

        if selectedOption == 1:
            createTicket(authToken)

        elif selectedOption == 2:
            listTickets()

        elif selectedOption == 3:
            deleteTicket(authToken)

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

    print("Digite os dados para adicionar tickets:")

    descriptionEvent = input("Descrição do Evento: ")
    eventName = input("Nome do evento: ")
    price = float(input("Preço: "))

    eventType = inquirer.select(
        message="Selecione o tipo de Ticket:",
        choices=[
            Choice(value="Show", name="Show"),
            Choice(value="StardUp", name="StardUp"),
        ],
        default=None,
    ).execute()

    headderTokenAuth = {"Authorization": "Bearer " + authToken}

    createTicketResponse = requests.post(
        ticketsResourceUrl,
        json={
            "description": descriptionEvent,
            "eventName": eventName,
            "price": price,
            "type": eventType,
        },
        headers=headderTokenAuth,
    )

    if createTicketResponse.status_code != 201:
        print("Erro interno ao tentar criar o ticket")
        return

    print("\nTicket criado com sucesso\n")


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


def deleteTicket(authToken):

    if not authToken:
        showFailedCredentialsMessage()
        return

    listTicketsResponse = requests.get(ticketsResourceUrl)
    responseTicketInJson = listTicketsResponse.json()

    nameTicketToBeDeleted = input("Escreva o nome do Ticket que deseja Deletar: ")

    headderTokenAuth = {"Authorization": "Bearer " + authToken}

    ticketId = 0
    for currentTicket in responseTicketInJson:
        if nameTicketToBeDeleted == currentTicket["eventName"]:
            ticketId = currentTicket["id"]

    ticketFiltredPerIdUrl = f"{ticketsResourceUrl}/{ticketId}"

    deleteTicketResponse = requests.delete(
        ticketFiltredPerIdUrl, headers=headderTokenAuth
    )

    if deleteTicketResponse.status_code != 200:
        print("Erro interno ao tentar excluir o ticket")
        return

    print("\nTicket Excluido com sucesso\n")
