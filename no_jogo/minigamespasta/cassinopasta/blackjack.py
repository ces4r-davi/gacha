import random

def hit():
    return random.randint(1, 11)

def mostrar_mao():
    print(f"Sua mão: {mao_jogador} = {sum(mao_jogador)}")
    print(f"Mão da mesa: {mao_dealer} = {sum(mao_dealer)}")

def blackjack(player):
    print("Bem vindo ao BlackJack")
    print("Regras: ")
    print("1- O jogador e a mesa receberá um número de 1 a 11 inicialmente, no qual ficará oculto a primeira carta da mesa.(Não tem ás)")
    print("2- O jogador poderá usar 3 comandos simples: \nPedir --> Pega mais uma carta\nParar --> Para com o seu jogo\nDobrar --> Dobra a aposta feita inicialmente.")
    print("3- A mesa irá pedir números até sua soma ser 17, caso some 17, irá parar de pedir cartas independente do que ocorrer.")
    print("4- Ganha quem possuir a maior soma, porém se o jogador ultrapassar a soma de 21 ele perde imediatamente.")
    print("5- Se o jogador e a mesa estourarem, a mesa é quem leva a aposta.")
    print("6- Se o jogador e a mesa alcançarem exatamente 21, o jogador é quem leva a aposta.\n\n")

    while True:
        print("O que deseja fazer: ")
        print("1 --> Jogar")
        print("0 --> Sair")
        try: 
            escolha = int(input("--> "))
        except:
            print("Digite uma escolha válida!")
        if escolha == 0:
            return
        if escolha == 1:

            global mao_jogador
            global mao_dealer
            mao_jogador = []
            mao_dealer = []
            dobrado = False
            print("BlackJack\n")

            try:
                print(f"Suas gemas: {player.gemas}")
                aposta = int(input("Informe sua aposta --> "))
                if aposta < 0:
                    print("A aposta deve ser um valor válido!")
                    continue
                elif aposta > player.gemas:
                    print("A aposta não pode ser mais do que você consegue pagar!")
                    continue
            except:
                print("A aposta deve ser um valor válido!")
                continue
            print("Primeira carta sorteada!")
            mao_jogador.append(hit())
            mao_dealer.append(hit())
            mostrar_mao()

            while sum(mao_jogador) < 21 and sum(mao_dealer) < 21:
                print("O que você deseja fazer?")
                print("1 --> Pedir")
                print("2 --> Parar")
                if not dobrado:
                    print("3 --> Dobrar")
                try:
                    acao = int(input("--> "))
                    if acao > 3 or acao < 1:
                        print("Escolha uma ação válida!")
                        continue
                except:
                    print("Escolha uma ação válida!")
                    continue
                if acao == 1:
                    mao_jogador.append(hit())
                    if sum(mao_dealer)<17:
                        mao_dealer.append(hit())
                    mostrar_mao()

                elif acao == 2:
                    while sum(mao_dealer) <17:
                        mao_dealer.append(hit())
                        mostrar_mao()
                    break

                elif acao == 3:
                    if not dobrado:
                        aposta *= 2
                        dobrado = True

                else:
                    print("Escolha uma ação válida!")
                        
            if sum(mao_jogador) == 21:
                print(f"Você cravou 21! Como prêmio você recebeu {aposta} gemas!")
                player.gemas += aposta
            elif sum(mao_jogador) <= 21:
                if sum(mao_dealer) > 21:
                    print(f"O dealer estourou!\nComo prêmio você recebeu {aposta} gemas!")
                    player.gemas+=aposta
                elif sum(mao_jogador) > sum(mao_dealer):
                    player.gemas+=aposta
                    print(f"Você venceu!\nComo prêmio você recebeu {aposta} gemas!")
                elif sum(mao_jogador) == sum(mao_dealer):
                    print("Houve empate!")
                else:
                    player.gemas-=aposta
                    print(f"Você perdeu...\nPerdeu {aposta} gemas...")
            else:
                player.gemas -= aposta
                print(f"Você estourou...\nPerdeu {aposta} gemas...")
        else:
            print("Digite uma escolha válida!")
