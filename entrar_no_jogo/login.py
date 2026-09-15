import os
import json
import hashlib
import uteis
from modelos.jogador import Jogador

def conferir():
    from main import inicializar
    dados_de_usuario = {}
    if os.path.exists("usuarios.json") and os.path.getsize("usuarios.json") > 0:
        with open("usuarios.json", 'r', encoding="utf-8") as arquivo:
            dados_de_usuario = json.load(arquivo)
        while True:
            nome_de_usuario = input("Digite seu nome(Digite \"0\" caso deseja voltar pra página inicial): ")
            if nome_de_usuario == '0':
                inicializar()
                return
            senha_do_usuario = input("Digite sua senha: ")
            senha_pura = senha_do_usuario.strip()
            senha_em_hash = hashlib.sha256(senha_pura.encode("utf-8")).hexdigest()
            if nome_de_usuario in dados_de_usuario:
                if senha_em_hash == dados_de_usuario[nome_de_usuario]["Senha"]:
                    uteis.limpar_tela()
                    print("Login realizado com sucesso!")
                    player_atual = Jogador(nome_de_usuario)
                    return player_atual
                else:
                    print("Senha Incorreta!")
            else:
                print("Usuário não encontrado...")
    else:
        print("Sem jogadores no momento.")
    