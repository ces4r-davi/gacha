import entrar_no_jogo.cadastro as cadastro
from rich import print
from uteis import limpar_tela
import modelos.jogador as jogador


player_atual = None
def fazer_cadastro():
    global player_atual
    from main import inicializar
    limpar_tela()
    print("[bold red]1- Fazer Cadastro:[/bold red]\n")
    nome_de_usuario = input("Digite o nome de usuário: ")
    sexo_do_usuario = input("Digite seu sexo[M/F]: ")
    senha_do_usuario = input("Digite sua senha: ")
    senha_repetida = input("Digite sua senha novamente: ")
    while(senha_do_usuario != senha_repetida):
        print("As senhas não se coincidem!")
        senha_do_usuario = input("Digite sua senha:")
        senha_repetida = input("Digite sua senha novamente: ")
    try:
        novo_usuario = cadastro.GerenciadorCadastro(nome_de_usuario, sexo_do_usuario, senha_do_usuario)
        novo_usuario.cadastrar()
        player_atual = jogador.Jogador(nome_de_usuario)
        print("Seus dados de usuário são: \n")
        print("[bold purple]Cadastro realizado com sucesso![/]")
        return player_atual
    except Exception as e:
        print(e)
        return




        
