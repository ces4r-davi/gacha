import random

def numero_unico():
    try:
        numero_apostado = int(input("Digite o número em que irá apostar --> "))
        if numero_apostado >= 0 and numero_apostado <=36:
            pass
        else:
            print("Digite um valor válido!")
    except:
        print("Digite um valor válido!")
    if numero_apostado == numero_sorteado:
        return True
    else:
        return False

def par_impar():
    try:
        numero_apostado = input("Digite se apostará em par ou ímpar[P/I] --> ").lower()
        if numero_apostado == 'p' or numero_apostado == 'i':
            pass
        else:
            print("Digite um valor válido!")
    except:
        print("Digite um valor válido!")
    if numero_apostado == 'p':
        if numero_sorteado%2 == 0:
            return True
        else:
            return False
    else:
        if numero_sorteado%2 == 0:
            return False
        else:
            return True
        
def metades():
    if numero_sorteado == 0:
        return False
    try:
        numero_apostado = int(input("Digite a metade em que irá apostar[1/2] --> "))
        if numero_apostado > 0 and numero_apostado <=2:
            pass
        else:
            print("Digite um valor válido!")
    except:
        print("Digite um valor válido!")
    if numero_apostado == 1:
        if numero_sorteado <= 18:
            return True
        else:
            return False
    else:
        if numero_sorteado > 18:
            return True
        else:
            return False

def duzias():
    if numero_sorteado == 0:
        return False
    try:
        numero_apostado = int(input("Digite a dúzia em que irá apostar[1/2/3] --> "))
        if numero_apostado > 0 and numero_apostado <=3:
            pass
        else:
            print("Digite um valor válido!")
    except:
        print("Digite um valor válido!")
    if numero_apostado == 1:
        if numero_sorteado <= 12:
            return True
        else:
            return False
    elif numero_apostado == 2:
        if numero_sorteado <=24 and numero_sorteado >12:
            return True
        else:
            return False
    else:
        if numero_sorteado > 24:
            return True
        else:
            return False

def coluna():
    colunas = {
    1: [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34],
    2: [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35],
    3: [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
}

    if numero_sorteado == 0:
        return False
    try:
        numero_apostado = int(input("Digite a coluna em que irá apostar[1/2/] --> "))
        if numero_apostado > 0 and numero_apostado <=3:
            pass
        else:
            print("Digite um valor válido!")
    except:
        print("Digite um valor válido!")
    if numero_apostado == 1:
        if numero_sorteado in colunas[1]:
            return True
        else:
            return False
    elif numero_apostado == 2:
        if numero_sorteado in colunas[2]:
            return True
        else:
            return False
    else:
        if numero_sorteado in colunas[3]:
            return True
        else:
            return False

def roleta(player):
    escolhas = {1:{numero_unico: 35}, 2:{par_impar: 1}, 3:{metades: 1}, 4:{duzias: 2}, 5:{coluna: 2}}
    print("Bem vindo ao Spin Attack")
    print("Regras:")
    print("1- A roleta possui 37 casas diferentes, possuindo também diferentes tipos de aposta: ")
    print("a) Número único. Você aposta um número especifico de 0 a 36. Em caso de acerto é retornado o valor de 35:1")
    print("b) Par ou Ímpar: Você aposta se o número será par ou ímpar. Em caso de acerto é retornado o valor de 1:1")
    print("c) Metades: Você aposta se o número será a primeira metade(1 a 18) ou segunda metade(19 a 36), o valor 0 não é considerado.")
    print("d) Dúzias: Você aposta qual dúzia o número pertence(Ex: 1° duzia: 1-12), o valor 0 não é considerado. Em caso de acerto é retornado o valor de 2:1")
    print("e) Coluna: Você aposta em qual das 3 colunas o número pertence(Ex: 1° coluna: 1, 4, 7...), o valor 0 não é considerado. Em caso de acerto é retornado o valor de 2:1")

    print("\nO que você deseja fazer?")
    while True:
        global numero_sorteado
        numero_sorteado = random.randint(0, 36)

        print("1 --> Jogar")
        print("0 -- > Sair")
        try:
            escolha = int(input("Digite a opção que você deseja: "))
            if escolha > 1 or escolha < 0:
                print("Digite uma opção válida!")
                continue
        except:
            print("Digite uma opção válida!")
            continue

        if escolha == 0:
            return
        elif escolha == 1:
            aposta = int(input("Digite o valor que deseja apostar: "))
            print("Qual será sua aposta?")
            print("1 --> Número único")
            print("2 --> Par ou ímpar")
            print("3 --> Metades")
            print("4 --> Dúzias")
            print("5 --> Coluna")
            try:
                escolha_aposta = int(input("--> "))
                if escolha_aposta > player.gemas:
                    print("Coloque um valor que caiba no seu bolso!")
                    continue
                elif escolha_aposta < 0:
                    print("Digite um valor válido!")
                    continue
            except:
                print("Digite um valor válido!")
            funcao, multiplicador = list(escolhas[escolha_aposta].items())[0]
            resultado = funcao()
            print(f"Número sorteado = {numero_sorteado}")
            if resultado:
                ganho = aposta*multiplicador
                print(f"Você acertou a aposta!!\nComo recompensa você recebeu {ganho} gemas!")
                player.gemas+=ganho
            else:
                print("Você perdeu a aposta...")
                player.gemas-=aposta



    