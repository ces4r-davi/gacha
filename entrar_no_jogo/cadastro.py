from rich import print
from rich.console import Console
from rich.table import Table
from modelos.personagens import malerover_personagem
from modelos.personagens import femrover_personagem
from modelos.tresestrelas import ARMA_3_ESTRELAS_LAMINA
import hashlib
import os
import json

console = Console()

class GerenciadorCadastro():
    def __init__(self, usuario, sexo, senha):
        self.usuario = usuario
        self.sexo = sexo
        self._senha = senha

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, valor):
        valor_limpo = valor.strip()
        if len(valor_limpo) < 3:
            raise ValueError("O nome de usuário precisa ter no mínimo 3 caracteres")
        elif ' ' in valor_limpo:
            raise ValueError("O nome de usuário não pode possuir espaços em branco.")
        self._usuario = valor_limpo

    @property
    def sexo(self):
        return self._sexo

    @sexo.setter
    def sexo(self, valor):
        sexos_disponiveis = ['M', 'F']
        self._sexo = valor.upper()
        if self._sexo not in sexos_disponiveis:
            raise ValueError("Sexo Inválido")

    def _criar_hash(self):
        senha_pura = self._senha.strip()
        if len(senha_pura) < 5:
            raise ValueError("A senha precisa ter no mínimo 5 caracteres.")
        if ' ' in senha_pura:
            raise ValueError("A senha não pode possuir espaços em branco.")
        senha_em_hash = hashlib.sha256(senha_pura.encode("utf-8")).hexdigest()
        return senha_em_hash

    def cadastrar(self):
        senha_em_hash = self._criar_hash()
        dados_existentes = {}
        if os.path.exists("usuarios.json") and os.path.getsize("usuarios.json") > 0:
            with open("usuarios.json", "r", encoding= "utf-8") as arquivo:
                dados_existentes = json.load(arquivo)

        if self.usuario in dados_existentes:
            raise ValueError(f"Um usuário com nome {self.usuario} ja existe.")


        if self.sexo == 'm' or self.sexo == 'M':
            personagem_principal = malerover_personagem.para_dict()
        else:
            personagem_principal = femrover_personagem           
        
        dados_existentes[self.usuario] = {
            "Senha": senha_em_hash,
            "Sexo": self.sexo, 
            "Gemas": 1600, 
            "Personagens": {
                personagem_principal: ARMA_3_ESTRELAS_LAMINA
            },
            "Inventário": {ARMA_3_ESTRELAS_LAMINA: personagem_principal},   
            "Ranking": 1,
            "Tiros": 0,
            "50/50": True,
            "Pity4Estrelas": 0,
            }

        with open("usuarios.json", "w", encoding="utf-8") as arquivo:
            json.dump(dados_existentes, arquivo, indent=4, ensure_ascii=False)

        tabela_jogador = Table(title= "Dados do Usuário: ")
        tabela_jogador.add_column("Rótulo", style = "bold purple")
        tabela_jogador.add_column("Conteúdo", style = "bold")
        tabela_jogador.add_row("Nome ", self.usuario)
        for chav, val in dados_existentes[self.usuario].items():
            if chav == "Senha":
                formatado = "******"
            elif chav == "50/50":
                if val == True:
                    formatado = "Sim"
                else:
                    formatado = "Não"
            elif isinstance(val, dict):
                formatado = ", ".join(val.keys())
            else:
                formatado = str(val)
            tabela_jogador.add_row(chav, formatado)
        console.print(tabela_jogador)
        

            

        

    

        