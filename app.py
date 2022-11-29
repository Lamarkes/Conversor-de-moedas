# Conversor de moedas, com objetivo de estudar e entender a utilizacao de APIs
# Utilizando requests, e a propria API economia.awesomeapi

"""O projeto consiste em puxar os valores atualizados das moedas: Dolar, Euro e Bitcoin e converter
 para a moeda brasileira."""

import requests  # importando o requests para consumir a API

requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
requisicao_dic = requisicao.json()  # convertendo para json, para utilizar no python como dicionarios


def estilizacao(texto):  # funcao de estilizacao
    print("-" * len(texto))
    print(texto)
    print("-" * len(texto))


def moedas():  # tabelas de moedas para serem escolhidas
    print("1- USD", "\n2- EUR", "\n3- BTC")


def converter(moeda_ini, moeada_de_cambio):  # algoritimo que faz o calculo do valor para real
    valor = moeda_ini / moeada_de_cambio
    return valor


while True:

    estilizacao("Conversor de Moedas")
    estilizacao("Valor Inicial")
    while True:
        try:
            valor_inicial = float(input("Insira o valor em REAL desejado que deseja converter: "))
            break
        except ValueError:
            print("Informe um valor valido!")

    estilizacao("Escolha a moeda que deseja: ")
    moeda_inicial = None
    simb = ""

    while moeda_inicial not in (1, 2, 3):
        moedas()

        try:
            moeda_inicial = int(input("Escolha uma das opções: "))
            if moeda_inicial == 1:
                simb = "USDBRL"
                print("Sua escolha: ", simb)
                break
            elif moeda_inicial == 2:
                simb = "EURBRL"
                print("Sua escolha: ", simb)
                break
            elif moeda_inicial == 3:
                simb = "BTCBRL"
                print("Sua escolha: ", simb)
                break
        except:
            print("Valor errado, selecione uma opção valida!")

    valor_final = float(requisicao_dic[simb]["bid"])

    valor_convertido = converter(valor_inicial, valor_final)

    if simb == "BTCBRL":
        print(f"O valor : ₿${valor_convertido}")
    elif simb == "USDBRL":
        print(f"O valor : US${valor_convertido:.2f}")
    else:
        print(f"O valor : Є${valor_convertido:.2f}")
