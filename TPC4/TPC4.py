import random


def criarLista():
    lista = []
    n = int(input("Quantos números quer na lista? "))

    i = 0
    while i < n:
        numero = random.randint(1, 100)
        lista.append(numero)
        i = i + 1

    return lista


def leLista():
    lista = []
    n = int(input("Quantos números quer na lista? "))

    i = 0
    while i < n:
        num = int(input("Introduza um número: "))
        lista.append(num)
        i = i + 1

    return lista


def somaLista(lista):
    soma = 0
    i = 0

    while i < len(lista):
        soma = soma + lista[i]
        i = i + 1

    return soma


def mediaLista(lista):
    soma = 0
    i = 0

    while i < len(lista):
        soma = soma + lista[i]
        i = i + 1

    media = soma / len(lista)

    return media


def maiorLista(lista):
    maior = lista[0]
    i = 0

    while i < len(lista):
        if lista[i] > maior:
            maior = lista[i]

        i = i + 1

    return maior


def menorLista(lista):
    menor = lista[0]
    i = 0

    while i < len(lista):
        if lista[i] < menor:
            menor = lista[i]

        i = i + 1

    return menor


def crescenteLista(lista):
    res = True
    i = 0

    while i < len(lista) - 1:
        if lista[i] > lista[i + 1]:
            res = False

        i = i + 1

    return res


def decrescenteLista(lista):
    res = True
    i = 0

    while i < len(lista) - 1:
        if lista[i] < lista[i + 1]:
            res = False

        i = i + 1

    return res


def procura(lista, elemento):
    posicao = -1
    i = 0

    while i < len(lista):
        if lista[i] == elemento and posicao == -1:
            posicao = i

        i = i + 1

    return posicao


lista = []

opcao = 1

while opcao > 0:

    print()
    print("(1) Criar Lista")
    print("(2) Ler Lista")
    print("(3) Soma")
    print("(4) Média")
    print("(5) Maior")
    print("(6) Menor")
    print("(7) Está ordenada por ordem crescente")
    print("(8) Está ordenada por ordem decrescente")
    print("(9) Procura um elemento")
    print("(0) Sair")
    print()

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:

        lista = criarLista()
        print("Lista criada:", lista)

    elif opcao == 2:

        lista = leLista()
        print("Lista criada:", lista)

    elif opcao == 3:

        if len(lista) > 0:
            print("A soma é:", somaLista(lista))
        else:
            print("Não existe nenhuma lista.")

    elif opcao == 4:

        if len(lista) > 0:
            print("A média é:", mediaLista(lista))
        else:
            print("Não existe nenhuma lista.")

    elif opcao == 5:

        if len(lista) > 0:
            print("O maior número é:", maiorLista(lista))
        else:
            print("Não existe nenhuma lista.")

    elif opcao == 6:

        if len(lista) > 0:
            print("O menor número é:", menorLista(lista))
        else:
            print("Não existe nenhuma lista.")

    elif opcao == 7:

        if len(lista) > 0:
            if crescenteLista(lista):
                print("Sim, a lista está ordenada por ordem crescente.")
            else:
                print("Não, a lista não está ordenada por ordem crescente.")
        else:
            print("Não existe nenhuma lista.")

    elif opcao == 8:

        if len(lista) > 0:
            if decrescenteLista(lista):
                print("Sim, a lista está ordenada por ordem decrescente.")
            else:
                print("Não, a lista não está ordenada por ordem decrescente.")
        else:
            print("Não existe nenhuma lista.")

    elif opcao == 9:

        if len(lista) > 0:
            elemento = int(input("Introduza o número que pretende procurar: "))
            posicao = procura(lista, elemento)
            print("Posição:", posicao)
        else:
            print("Não existe nenhuma lista.")

    elif opcao == 0:

        print("O programa terminou.")
        print("Lista que ficou guardada:", lista)

    else:

        print("Opção inválida.")