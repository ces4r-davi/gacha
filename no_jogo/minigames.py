from uteis import limpar_tela
from no_jogo.minigamespasta.termo import termo
from no_jogo.minigamespasta.cassinopasta.menucassino import menu_cassino
from no_jogo.minigamespasta.torre_da_adversidade import torre_da_adversidade

def minigames(player):
    from menu import menu
    while True:
        limpar_tela()
        escolhas = {1:torre_da_adversidade, 2:termo, 3:menu_cassino}
        print("Bem vindo aos minigames do Refactory!")
        print("Qual jogo você deseja?\n")
        print("1 --> Torre da Adversidade")
        print("2 --> Termo")
        print("3 --> Cassino")
        print("0 --> Voltar ao Menu")
        escolha = int(input("Digite a opção que deseja --> "))
        escolhas[escolha](player)
