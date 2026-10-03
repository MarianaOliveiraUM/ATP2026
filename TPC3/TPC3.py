def corrida():

    jogar = "Sim"

    while jogar == "Sim":

        print("JOGO CORRIDA PARA O 100")
        print("Em cada jogada pode acrescentar um número de 1 a 10. Vence quem atingir o 100.")
        print("1 - O computador joga primeiro.")
        print("2 - O utilizador joga primeiro.")

        opcao = int(input("Escolha a modalidade: "))

        if opcao == 1:

            total = 0
            acertou = False

            while acertou == False:

                if total == 0:
                    jogada = 1
                else:
                    jogada = 11 - jogada_utilizador

                total = total + jogada

                print("O computador acrescentou:", jogada)
                print("Total:", total)

                if total == 100:
                    print("O computador venceu!")
                    acertou = True

                else:
                    jogada_utilizador = int(input("Quanto quer acrescentar (1 a 10)? "))

                    while jogada_utilizador < 1 or jogada_utilizador > 10:
                        print("Escolha um número entre 1 e 10.")
                        jogada_utilizador = int(input("Quanto quer acrescentar (1 a 10)? "))

                    total = total + jogada_utilizador

                    print("Total:", total)

                    if total == 100:
                        print("O utilizador venceu!")
                        acertou = True

        elif opcao == 2:

            total = 0
            acertou = False
            primeira_jogada = True

            while acertou == False:

                jogada_utilizador = int(input("Quanto quer acrescentar (1 a 10)? "))

                while jogada_utilizador < 1 or jogada_utilizador > 10:
                    print("Escolha um número entre 1 e 10.")
                    jogada_utilizador = int(input("Quanto quer acrescentar (1 a 10)? "))

                total = total + jogada_utilizador

                print("Total:", total)

                if total == 100:
                    print("O utilizador venceu!")
                    acertou = True

                else:
                    if primeira_jogada == True:
                        if jogada_utilizador == 1:
                            jogada = 10
                        else:
                            jogada = 12 - jogada_utilizador

                        primeira_jogada = False

                    else:
                        jogada = 11 - jogada_utilizador

                    total = total + jogada

                    print("O computador acrescentou:", jogada)
                    print("Total:", total)

                    if total == 100:
                        print("O computador venceu!")
                        acertou = True

        else:
            print("Opção inválida")

        jogar = input("Quer jogar novamente? (Sim/Não): ")

    print("Obrigado por jogar!")
corrida()