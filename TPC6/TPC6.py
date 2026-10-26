import matplotlib.pyplot as plt

def medias(tabMeteo):
    res = []
    for data, tmin, tmax, p in tabMeteo:
        media = (tmin + tmax) / 2
        res.append((data, media))
    return res


def guardaTabMeteo(t, fnome):
    file = open(fnome, "w")
    for data, tmin, tmax, p in t:
        ano, mes, dia = data
        file.write(f"{ano}-{mes}-{dia}|{tmin}|{tmax}|{p}\n")
    file.close()
    return


def carregaTabMeteo(fnome):
    res = []
    file = open(fnome, "r")

    for line in file:
        data, tmin, tmax, p = line.split("|")
        ano, mes, dia = data.split("-")
        data = (int(ano), int(mes), int(dia))

        res.append((data, float(tmin), float(tmax), float(p)))

    file.close()
    return res


def minMin(tabMeteo):
    minima = tabMeteo[0][1]

    for data, tmin, tmax, p in tabMeteo:
        if tmin < minima:
            minima = tmin

    return minima


def amplTerm(tabMeteo):
    res = []

    for data, tmin, tmax, p in tabMeteo:
        amplitude = tmax - tmin
        res.append((data, amplitude))

    return res


def maxChuva(tabMeteo):
    max_data = tabMeteo[0][0]
    max_prec = tabMeteo[0][3]

    for data, tmin, tmax, p in tabMeteo:
        if p > max_prec:
            max_data = data
            max_prec = p

    return (max_data, max_prec)


def diasChuvosos(tabMeteo, p):
    res = []

    for data, tmin, tmax, prec in tabMeteo:
        if prec > p:
            res.append((data, prec))

    return res


def maxPeriodoCalor(tabMeteo, p):
    maior = 0
    atual = 0

    for data, tmin, tmax, prec in tabMeteo:
        if prec < p:
            atual = atual + 1

            if atual > maior:
                maior = atual
        else:
            atual = 0

    return maior


def grafTabMeteo(t):
    datas = []
    y_min = []
    y_max = []
    y_prec = []

    for data, tmin, tmax, p in t:
        datas.append(f"{data[0]}-{data[1]}-{data[2]}")
        y_min.append(tmin)
        y_max.append(tmax)
        y_prec.append(p)

    plt.figure()
    plt.plot(datas, y_min, marker="o",
             label="Temperatura minima (ºC)")
    plt.plot(datas, y_max, marker="o",
             label="Temperatura maxima (ºC)")
    plt.xlabel("Data")
    plt.ylabel("Temperatura (ºC)")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    plt.figure()
    plt.plot(datas, y_prec, marker="o",
             label="Precipitacao")
    plt.xlabel("Data")
    plt.ylabel("Precipitacao")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    return


def mostrarData(data):
    ano, mes, dia = data
    return f"{dia}/{mes}/{ano}"


def mostrarTabela(tabMeteo):
    for data, tmin, tmax, p in tabMeteo:
        print(mostrarData(data),"- Mínima:", tmin, "ºC", "- Máxima:", tmax, "ºC","- Precipitação:", p)


def criarTabela():
    res = []
    n = int(input("Quantos dias quer inserir? "))

    for i in range(n):
        print("Dia", i + 1)

        ano = int(input("Ano: "))

        mes = int(input("Mês (1 a 12): "))
        while mes < 1 or mes > 12:
            print("Mês inválido! Insira um mês entre 1 e 12.")
            mes = int(input("Mês (1 a 12): "))

        dia = int(input("Dia (1 a 31): "))
        while dia < 1 or dia > 31:
            print("Dia inválido! Insira um dia entre 1 e 31.")
            dia = int(input("Dia (1 a 31): "))

        tmin = float(input("Temperatura mínima: "))
        tmax = float(input("Temperatura máxima: "))
        p = float(input("Precipitação: "))

        res.append(((ano, mes, dia), tmin, tmax, p))

    return res


tabMeteo = [((2022, 1, 20), 2, 16, 0), ((2022, 1, 21), 1, 13, 0.2), ((2022, 1, 22), 7, 17, 0.01)]

ficheirosGuardados = []

opcao = ""

while opcao != "0":
    print("APLICACAO DE METEOROLOGIA")
    print("1 - Criar uma tabela meteorologica")
    print("2 - Mostrar a tabela")
    print("3 - Calcular as temperaturas médias")
    print("4 - Calcular a temperatura mínima mais baixa")
    print("5 - Calcular as amplitudes térmicas")
    print("6 - Encontrar o dia com maior precipitação")
    print("7 - Mostrar os dias com precipitação acima de um limite")
    print("8 - Calcular o maior periodo consecutivo abaixo de um limite")
    print("9 - Desenhar os gráficos")
    print("10 - Guardar a tabela num ficheiro")
    print("11 - Carregar uma tabela de um ficheiro")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tabMeteo = criarTabela()
        print("Tabela criada com sucesso!")

    elif opcao == "2":
        if len(tabMeteo) > 0:
            mostrarTabela(tabMeteo)
        else:
            print("A tabela está vazia.")

    elif opcao == "3":
        if len(tabMeteo) > 0:
            resultado = medias(tabMeteo)

            for data, media in resultado:
                print(mostrarData(data),
                      "- Temperatura média:", media, "ºC")
        else:
            print("A tabela está vazia.")

    elif opcao == "4":
        if len(tabMeteo) > 0:
            print("Temperatura mínima mais baixa:",
                  minMin(tabMeteo), "ºC")
        else:
            print("A tabela está vazia.")

    elif opcao == "5":
        if len(tabMeteo) > 0:
            resultado = amplTerm(tabMeteo)

            for data, amplitude in resultado:
                print(mostrarData(data),
                      "- Amplitude térmica:", amplitude, "ºC")
        else:
            print("A tabela está vazia.")

    elif opcao == "6":
        if len(tabMeteo) > 0:
            data, prec = maxChuva(tabMeteo)
            print("Dia com maior precipitação:", mostrarData(data))
            print("Precipitação:", prec)
        else:
            print("A tabela está vazia.")

    elif opcao == "7":
        if len(tabMeteo) > 0:
            limite = float(input("Introduza o limite de precipitação: "))
            resultado = diasChuvosos(tabMeteo, limite)

            if len(resultado) > 0:
                for data, prec in resultado:
                    print(mostrarData(data), "- Precipitação:", prec)
            else:
                print("Não existem dias acima desse limite.")
        else:
            print("A tabela está vazia.")

    elif opcao == "8":
        if len(tabMeteo) > 0:
            limite = float(input("Introduza o limite de precipitação: "))
            resultado = maxPeriodoCalor(tabMeteo, limite)
            print("Maior número de dias consecutivos abaixo do limite:", resultado)
        else:
            print("A tabela está vazia.")

    elif opcao == "9":
        if len(tabMeteo) > 0:
            grafTabMeteo(tabMeteo)
        else:
            print("A tabela está vazia.")

    elif opcao == "10":
        nome = input("Nome do ficheiro para guardar (ex: meteorologia.txt): ")
        guardaTabMeteo(tabMeteo, nome)
        if nome not in ficheirosGuardados:
            ficheirosGuardados.append(nome)
        print("Tabela guardada com sucesso!")

    elif opcao == "11":
        fnome = input("Nome do ficheiro a carregar: ")

        while nome not in ficheirosGuardados:
            print("Ficheiro não encontrado! Insira o nome novamente.")
            fnome = input("Nome do ficheiro a carregar: ")

        print(carregaTabMeteo(fnome))

    elif opcao == "0":
        print("A sair da aplicação...")

    else:
        print("Opcao inválida!")