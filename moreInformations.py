import requests
import matplotlib.pyplot as plt

from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from itertools import groupby, count
from operator import itemgetter

from constants import ticketsResourceUrl, userResourceUrl

from helpers.menu import showWrongMenuMessage, goBackMenuMessage, exitApp, confirmBack
from helpers.clean import clean


def showMoreInformationMenu():
    while True:
        clean()
        selectMenu = inquirer.select(
            message="Mais Informações e Opções da APi:",
            choices=[
                Choice(value=1, name="Grafico de Número de Tickets de um Tipo"),
                Choice(value=2, name="Listar Numero de Tickets por Usuario"),
                Choice(value=3, name="Voltar"),
            ],
            default=None,
        ).execute()

        if selectMenu == 1:
            filtedTicketsPerType()

        elif selectMenu == 2:
            numberTicketsPerUser()

        elif selectMenu == 3:
            goBackMenuMessage()
            break

        else:
            showWrongMenuMessage()


def filtedTicketsPerType():
    print("Grafico Filtrado por Tipo de Tickets")
    print("\n")

    isShow = 0
    isStardUp = 0

    listTicketsResponse = requests.get(ticketsResourceUrl)
    responseInJson = listTicketsResponse.json()

    if listTicketsResponse.status_code != 200:
        print("Erro... Não foi possível trazer os dados de tickets")
        confirmBack()
        return

    if len(responseInJson) == 0:
        print("Não há tickets cadastrados\n")
        confirmBack()
        return

    for isCurrentTicketType in responseInJson:
        if isCurrentTicketType["type"] == "Show":
            isShow += 1
        else:
            isStardUp += 1
    
    
    fig, ax = plt.subplots()

    textTicket = ('Show', 'StardUp')
    numberTypeTickets = (isShow, isStardUp)
    y_position = range(len(textTicket))

    ax.barh(y_position, numberTypeTickets, align='center')
    ax.set_yticks(y_position, labels=textTicket)
    ax.set_xlabel('Registro de Venda de Tickets')
    ax.set_title('Registro de venda de ingressos por tipo')

    plt.show()


def numberTicketsPerUser():
    print("Numero de Tickets Comprado Por Usuarios")

    listTicketsResponse = requests.get(ticketsResourceUrl)
    listUsersResponse = requests.get(userResourceUrl)
    
    responseTicketInJson = listTicketsResponse.json()
    responseUserInJson = listUsersResponse.json()
    

    if listTicketsResponse.status_code != 200:
        print("Erro... Não foi possível trazer os dados de tickets")
        confirmBack()
        return

    if len(responseTicketInJson) == 0:
        print("Não há tickets cadastrados\n")
        confirmBack()
        return
    
    print("\n")
    print("# Usuario " + "-"*30 + " Total Tickets")
    print("\n")

    for key, value in groupby(responseTicketInJson, key=itemgetter("userId")):
        for currentUser in responseUserInJson:
            if currentUser["id"] == key:
                print(f"> {currentUser["name"]:7s} {"=" *30} { len(list(value))} Tickets Comprados ")
    print("\n")
    
    confirmBack()

