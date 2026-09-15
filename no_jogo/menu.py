from rich import print
from no_jogo.minigames import minigames
from no_jogo.ficha import exibir_ficha
from no_jogo.inventario import exibir_inventario
from modelos.jogador import Jogador
from modelos.banners.banneraemeath import BannerAemeath
def menu(player):
    while True:
        from main import inicializar
        print("O que deseja fazer?\n")
        print("1 --> Minigames")
        print("2 --> Gacha")
        print("3 --> Inventário")
        print("4 --> Ficha do Jogador")
        print("5 --> Salvar Jogo")
        print("0 --> Sair")
        escolha = int(input("\nQual opção você deseja --> "))
        if escolha == 1:
            minigames(player)
        elif escolha == 2:
            BannerAemeath.pull_aemeath(player)
        elif escolha == 3:
            exibir_inventario(player)
        elif escolha == 4:
            exibir_ficha(player)
        elif escolha == 5:
            Jogador.salvar_no_json(player)
        elif escolha == 0:
            return
            
