import requests
from itertools import groupby, count
from operator import itemgetter
import matplotlib.pyplot as plt

from constants import ticketsResourceUrl, userResourceUrl

from helpers.menu import showWrongMenuMessage, goBackMenuMessage


def showMoreInformationMenu():
    while True:
        print("1. Grafico de Número de Tickets de um Tipo")
        print("2. Listar Numero de Tickets por Usuario")
        print("9. Voltar")

        selectedOption = int(input("Opção: "))
        print("\n")

        if selectedOption == 1:
            filtedTicketsPerType()

        elif selectedOption == 2:
            numberTicketsPerUser()

        elif selectedOption == 9:
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
        return

    if len(responseInJson) == 0:
        print("Não há tickets cadastrados\n")
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
        return

    if len(responseTicketInJson) == 0:
        print("Não há tickets cadastrados\n")
        return
    
    print("\n")
    print("# Usuario " + "-"*30 + " Total Tickets")
    print("\n")

    for key, value in groupby(responseTicketInJson, key=itemgetter("userId")):
        for currentUser in responseUserInJson:
            if currentUser["id"] == key:
                print(f"> {currentUser["name"]:7s} {"=" *30} { len(list(value))} Tickets Comprados ")
    print("\n")

