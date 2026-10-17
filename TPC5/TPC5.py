def criarTurma():
    turma = []
    print("Turma criada com sucesso!")
    return turma


def lerNotatpc():
    nota = float(input("Introduza a nota do TPC (de 0 a 200): "))

    while nota < 0 or nota > 200:
        nota = float(input("A nota tem de estar entre 0 e 200. Introduza novamente: "))

    return nota

def lerNotaproj():
    nota = float(input("Introduza a nota do projeto (de 0 a 200): "))

    while nota < 0 or nota > 200:
        nota = float(input("A nota tem de estar entre 0 e 200. Introduza novamente: "))

    return nota

def lerNotateste():
    nota = float(input("Introduza a nota do teste (de 0 a 200): "))

    while nota < 0 or nota > 200:
        nota = float(input("A nota tem de estar entre 0 e 200. Introduza novamente: "))

    return nota


def inserirAluno(turma):

    nome = input("Nome do aluno: ")
    id = input("ID do aluno: ")

    notaTPC = lerNotatpc()
    notaProj = lerNotaproj()
    notaTeste = lerNotateste()

    notas = [notaTPC, notaProj, notaTeste]
    aluno = (nome, id, notas)

    turma.append(aluno)

    print("Aluno inserido com sucesso!")
    return turma


def listarTurma(turma):
    if len(turma) == 0:
        print("A turma está vazia!")
    else:
        print("Lista de Alunos:")
        for aluno in turma:
            nome = aluno[0]
            id = aluno[1]
            notas = aluno[2]
            print(f"Nome: {nome} | ID: {id} | Notas (TPC, Proj, Teste): {notas}")
    return turma


def idAluno(turma):
    id = input("Introduza o ID do aluno: ")

    i = 0
    encontrado = False
    aluno_encontrado = ()

    while i < len(turma) and encontrado == False:
        if turma[i][1] == id:
            aluno_encontrado = turma[i]

            print("Nome:", aluno_encontrado[0])
            print("ID:", aluno_encontrado[1])
            print("Nota TPC:", aluno_encontrado[2][0])
            print("Nota Projeto:", aluno_encontrado[2][1])
            print("Nota Teste:", aluno_encontrado[2][2])

            encontrado = True

        i = i + 1

    if encontrado == False:
        print("Aluno não encontrado.")

    return aluno_encontrado


def guardarTurma(turma):
    file = open("turma.txt", "w")

    for aluno in turma:
        nome, id, notas = aluno

        file.write(f"{nome}#{id}#{notas[0]}#{notas[1]}#{notas[2]}\n")

    file.close()

    print("Turma guardada com sucesso!")
    return turma



def carregarTurma():
    turma = []
    file = open("turma.txt", "r")

    for line in file:
        dados = line.split("#")

        nome = dados[0]
        id = dados[1]
        notaTPC = float(dados[2])
        notaProj = float(dados[3])
        notaTeste = float(dados[4])

        notas = [notaTPC, notaProj, notaTeste]
        aluno = (nome, id, notas)

        turma.append(aluno)

    file.close()
    return turma


turma = []
turma_criada = False
turma_guardada = False

opcao = ""

while opcao != "0":
    print("GESTÃO DE ALUNOS:")
    print("1 - Criar uma turma")
    print("2 - Inserir um aluno na turma")
    print("3 - Listar a turma")
    print("4 - Consultar um aluno por ID")
    print("8 - Guardar a turma em ficheiro")
    print("9 - Carregar uma turma dum ficheiro")
    print("0 - Sair da aplicação")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        turma = criarTurma()
        turma_criada = True
        turma_guardada = False

    elif opcao == "2":
        if turma_criada == False:
            print("É necessário criar uma turma primeiro!")
        else:
            turma = inserirAluno(turma)

    elif opcao == "3":
        if turma_criada == False:
            print("É necessário criar uma turma primeiro!")
        else:
            turma = listarTurma(turma)

    elif opcao == "4":
        if turma_criada == False:
            print("É necessário criar uma turma primeiro!")
        else:
            aluno = idAluno(turma)

    elif opcao == "8":
        if turma_criada == False:
            print("É necessário criar uma turma primeiro!")
        else:
            turma = guardarTurma(turma)
            turma_guardada = True

    elif opcao == "9":
        turma = carregarTurma()
        turma_criada = True
        turma_guardada = True
        print("Turma carregada com sucesso!")
        listarTurma(turma)


    elif opcao == "0":
        print("Aplicação encerrada.")

    else:
        print("Opção inválida. Tente novamente.")

