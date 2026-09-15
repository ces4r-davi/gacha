from rich import print
import uteis
from entrar_no_jogo.cadastrar import fazer_cadastro
from entrar_no_jogo.login import conferir
from no_jogo.menu import menu
def sair_do_jogo():
    escolha_sair = input("Tem certeza que deseja sair do jogo? --> ").lower().strip()
    if escolha_sair in uteis.RESPOSTAS_SIM:
        uteis.limpar_tela()
        print("Até mais!!\n")
        print("Saindo do jogo...")
        return 0
    elif escolha_sair in uteis.RESPOSTAS_NAO:
        uteis.limpar_tela()
        inicializar()
    else:
        print("Resposta inválida!")
        sair_do_jogo()

def inicializar():
    print("\n\nBem vindo ao [bold purple]Refactory[/]! Para continuar, por favor realize o [bold white]cadastro[/] ou o [bold white]login[/].")
    print("[bold white]Sair do jogo[/] --> 0")
    print("[bold white]Fazer Cadastro[/] --> 1")
    print("[bold white]Fazer Login[/] --> 2\n")
    numero_escolhido = int(input("Qual das opções você deseja(0/1/2)? --> "))
    if numero_escolhido == 1:
        player_atual = fazer_cadastro()
    elif numero_escolhido == 2:
        player_atual = conferir()
    elif numero_escolhido == 0:
        sair_do_jogo()
    else:
        uteis.limpar_tela()
        print("[bold white]Opção inválida![/]\n")
        inicializar()
    if player_atual:
        menu(player_atual)
def main():
    inicializar()

if __name__ == "__main__":
    main()

