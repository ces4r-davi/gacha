import random

def maior_ou_menor(player):
    gemas = 10000000000000
    print("Bem vindo ao jogo de Maior ou Menor!")
    print("Regras: ")
    print("1- Será sorteado um número entre 1 e 20, após isso você deverá dizer se o próximo número sorteado é maior, menor ou igual ao valor sorteado no momento.")
    print("2- Caso acerte tanto em menor ou maior, você receberá o dobro do que apostou, porém se perder perderá a aposta inteira.")
    print("3- Caso aposte em mesmo valor, se acertar você recebe 16x o valor apostado, e se perder perderá a aposta inteira da mesma forma.")
    while True:
        print("\nEscolha a opção que deseja: ")
        print("1- Ir para o jogo")
        print("0- Sair do jogo")
        try:
            escolha = int(input("Digite qual opção você deseja --> "))
            if escolha > 1 or escolha < 0:
                print("Insira um valor válido")
                continue
        except:
            print("Digite um valor válido.")
            continue
        if escolha == 0:
            return
        elif escolha == 1:
            while True:
                numero_sorteado = random.randint(1, 20)
                numero_sorteado_em_seguida = random.randint(1, 20)
                print("Jogo começou!")
                print(f"\nO valor sorteado é {numero_sorteado}")
                try:
                    quantia = int(input("Faça sua aposta --> "))
                    if quantia<0:
                        print("Digite um valor valido.")
                        continue
                    elif quantia>gemas:
                        print("Digite um valor que caiba no seu bolso.")
                        continue
                except:
                    print("Digite um valor válido!")
                    continue
                aposta = int(input("Você acredita que será:\n1- Maior\n2- Menor\n3- Empate\n--> "))
                print(f"O valor sorteado foi {numero_sorteado_em_seguida}")
                if aposta == 1:
                    if numero_sorteado<numero_sorteado_em_seguida:
                        ganho = quantia*2
                        gemas += ganho
                        print(f"Você acertou a aposta!\nVocê recebeu {ganho} gemas!")
                    else:
                        print("Você errou a aposta...\n")
                if aposta == 2:
                    if numero_sorteado>numero_sorteado_em_seguida:
                        ganho = quantia*2
                        gemas+= ganho
                        print(f"Você acertou a aposta!\nVocê recebeu {ganho} gemas!")
                    else:
                        print("Você errou a aposta...\n")
                if aposta == 3:
                    if numero_sorteado == numero_sorteado_em_seguida:
                        ganho = quantia*16
                        gemas+=ganho
                        print(f"Você acertou a sorte grande!!\nVocê recebeu{ganho} gemas!")
                    else:
                        print("Você errou a aposta...")
                continuar = input("Deseja continuar?[S/N] --> ").lower()
                if continuar == 's':
                    continue
                else:
                    break
