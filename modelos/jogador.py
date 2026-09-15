import os
import json

class Jogador:
    def __init__(self, nome):
        self._nome = nome
        dados_de_usuario = {}
        
        if os.path.exists("usuarios.json") and os.path.getsize("usuarios.json") > 0:
            with open("usuarios.json", 'r', encoding="utf-8") as arquivo:
                dados_de_usuario = json.load(arquivo)
        self._senha = dados_de_usuario[self._nome]["Senha"]
        self._sexo = dados_de_usuario[self._nome]["Sexo"]
        self._gemas = dados_de_usuario[self._nome]["Gemas"]
        self._itens = dados_de_usuario[self._nome]["Inventário"]
        self._personagens = dados_de_usuario[self._nome]["Personagens"]
        self._rank = dados_de_usuario[self._nome]["Ranking"]
        self._pity = dados_de_usuario[self._nome]["Tiros"]
        self._cinquentacinquenta = dados_de_usuario[self._nome]["50/50"]
        self._pity4estrelas = dados_de_usuario[self._nome]["Pity4Estrelas"]

    @property
    def nome(self):
        return self._nome

    @property
    def sexo(self):
        return self._sexo

    @property
    def gemas(self):
        return self._gemas

    @gemas.setter
    def gemas(self, valor):
        self._gemas = valor

    @property
    def itens(self):
        return self._itens

    @property
    def personagens(self):
        return self._personagens

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, valor):
        self._rank = valor

    @property
    def pity(self):
        return self._pity

    @pity.setter
    def pity(self, valor):
        self._pity = valor

    @property
    def cinquentacinquenta(self):
        return self._cinquentacinquenta

    @cinquentacinquenta.setter
    def cinquentacinquenta(self, estado):
        self._cinquentacinquenta = estado

    @property
    def pity4estrelas(self):
        return self._pity4estrelas

    @pity4estrelas.setter
    def pity4estrelas(self, valor):
        self._pity4estrelas=valor

    def para_dict(self):
        inventario_para_json = {}
        personagens_para_json = {personagens.para_dict() for personagens in self._personagens.items()}
        for item, dono in self._itens.items():
            if isinstance(item, str):
                inventario_para_json[item] = dono
            else:
                inventario_para_json[item.nome] = dono
        return{
            "Senha": self._senha,
            "Sexo": self._sexo,
            "Gemas": self._gemas,
            "Inventário": inventario_para_json,
            "Personagens": personagens_para_json,
            "Ranking": self._rank,
            "Pity": self._pity,
            "50/50": self._cinquentacinquenta,
            "Pity4Estrelas": self._pity4estrelas,
        }

    def salvar_no_json(self, caminho="usuarios.json"):

        dados_do_usuario = {}
        if(os.path.exists(caminho) and os.path.getsize(caminho) >0):
            with open("usuarios.json", 'r', encoding="utf-8") as arquivo:
                dados_do_usuario = json.load(arquivo)
            dados_do_usuario[self.nome] = self.para_dict()
            with open("usuarios.json", 'w', encoding="utf-8") as arquivo:
                json.dump(dados_do_usuario, arquivo, indent=4, ensure_ascii=False)
        

        