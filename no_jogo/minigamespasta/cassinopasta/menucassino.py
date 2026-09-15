from no_jogo.minigamespasta.cassinopasta.blackjack import blackjack
from no_jogo.minigamespasta.cassinopasta.cara_ou_coroa import cara_ou_coroa
from no_jogo.minigamespasta.cassinopasta.maior_menor import maior_ou_menor
from no_jogo.minigamespasta.cassinopasta.roleta import roleta

def menu_cassino(player):
    lista = {1:blackjack, 2:cara_ou_coroa, 3:maior_ou_menor, 4:roleta}
    while True:
        print("Bem vindo ao Cassino!!")
        print("Escolha o jogo que deseja: ")
        print("1- BlackJack")
        print("2- Cara ou Coroa")
        print("3- Maior ou Menor")
        print("4- Roleta")
        try:
            escolha = int(input("--> "))
            if escolha > 4 or escolha < 0:
                print("Digite uma opção válida.")
                continue
        except:
            print("Digite uma opção válida!")
            continue
        if escolha == 0:
            return
        else:
            lista[escolha](player)
        