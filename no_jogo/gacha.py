from rich import print

def escolher_banner(player):
    from menu import menu
    escolhas = {1:"a", 0: menu}
    print("Bem vindo aos banners!")
    banner_1 = 1
    print("Qual banner você deseja atirar?\n")
    print("1 --> Banner da Aemeath")
    print("0 --> Voltar ao Menu")
    escolha = int(input("Digite qual opção você deseja -->"))
    escolhas[escolha]()
    