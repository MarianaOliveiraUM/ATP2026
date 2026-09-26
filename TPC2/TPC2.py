import random


def adivinha():

    jogar = "Sim"

    while jogar == "Sim":

        print("JOGO ADIVINHA O NÚMERO")
        print("O número está entre 0 e 100, inclusive.")
        print("1 - O computador pensa num número")
        print("2 - O utilizador pensa num número")

        opcao = int(input("Escolha a modalidade: "))

        if opcao == 1:

            numero = random.randint(0, 100)
            tentativas = 0
            acertou = False

            while acertou == False:

                tentativa = int(input("Tente adivinhar o número: "))
                tentativas = tentativas + 1

                if tentativa == numero:
                    print("Acertou!")
                    acertou = True

                elif tentativa < numero:
                    print("O número que pensei é Maior")

                else:
                    print("O número que pensei é Menor")

            print("Número de tentativas:", tentativas)

        elif opcao == 2:

            print("Pense num número entre 0 e 100, inclusive.")

            menor = 0
            maior = 100
            tentativas = 0
            acertou = False

            while acertou == False:

                numero = (menor + maior) // 2
                tentativas = tentativas + 1

                print("O meu palpite é:", numero)

                resposta = input("Escreva Acertou, Maior ou Menor: ")

                if resposta == "Acertou":
                    acertou = True

                elif resposta == "Maior":
                    menor = numero + 1

                elif resposta == "Menor":
                    maior = numero - 1

            print("O computador acertou em", tentativas, "tentativas")

        else:
            print("Opção inválida")

        jogar = input("Quer jogar novamente? (Sim/Não): ")

    print("Obrigado por jogar!")


adivinha()