from abc import ABC, abstractmethod

class PersonagemBase(ABC):
    def __init__(self, nome, raridade, elemento, dano_base, taxa_crit, dano_crit, hp, level, energia, resistencia, escudo, arma):
        self.nome = nome
        self.raridade = raridade
        self.elemento = elemento
        self.dano_base = dano_base
        self.taxa_crit = taxa_crit
        self.dano_crit = dano_crit
        self.hp = hp
        self.level = level
        self.energia = energia
        self.resistencia = resistencia
        self.escudo = escudo
        self.arma = arma
        
    def para_dict(self) -> dict:
        return{self.nome: self.arma}

    @staticmethod
    def criar_catalogo()

    def dano_recebido(self, dano_bruto = int):
        dano_total = dano_recebido = dano_bruto/self.resistencia
        print(f"{self.nome} perdeu {dano_total} de hp...")
        self.hp -= dano_total

    def dano_recebido_em_porcentagem(self, dano_porcento = int):
        print(f"{self.nome} perdeu {dano_porcento}% de vida...")
        self.hp = self.hp - self.hp*(dano_porcento/100)

    def diminuir_resistencia(self, debuff = int):
        print(f"{self.nome} perdeu {debuff}% de resistencia...")
        res -= debuff

    def ganhar_escudo(self, escudos = int):
        print(f"{self.nome} ganhou {escudos} escudo(s)!")

    def perder_escudo(self, escudos):
        print(f"{self.nome} perdeu {escudos} escudo(s)...")
        

    @abstractmethod
    def atacar_normal(self):
        print(f"{self.nome} usou ataque normal...")
        return self.dano_base

    @abstractmethod
    def habilidade_de_ressonancia(self):
        pass

    @abstractmethod
    def liberacao_de_ressonancia(self):
        pass

class MaleRover(PersonagemBase):
    def __init__(self):
        super().__init__(nome="Male Rover", raridade="5*", elemento="Espectro", dano_base=50, taxa_crit=0.05, dano_crit= 0.5, hp = 1000, level = 1, energia = 0, resistencia= 1, escudo=0)

    def atacar_normal(self):
        return super().atacar_normal()

    def habilidade_de_ressonancia(self):
        print(f"{self.nome} usou Corte Lumen...")
        return self.dano_base*4

    def liberacao_de_ressonancia(self):
        print(f"{self.nome} usou Luz Espinhal...")
        return self.dano_base*10*(1+self.dano_crit)

class FemRover(PersonagemBase):
    def __init__(self):
        super().__init__(nome="Fem Rover", raridade="5*", elemento="Espectro", dano_base=60, taxa_crit=0.05, dano_crit= 0.5, hp = 800, level = 1, energia = 0, resistencia= 1, escudo=0)

    def atacar_normal(self):
        return super().atacar_normal()

    def habilidade_de_ressonancia(self):
        print(f"{self.nome} usou Corte Lumen...")
        return self.dano_base*4

    def liberacao_de_ressonancia(self):
        print(f"{self.nome} usou Luz Espinhal...")
        return self.dano_base*10*(1+self.dano_crit)

class Aemeath(PersonagemBase):
    def __init__(self):
        super().__init__(nome="Aemeath", raridade="5*", elemento="Térmico", dano_base=80, taxa_crit=0.05, dano_crit=0.5, hp = 1200, level = 1, energia = 0, resistencia = 1, escudo = 0)

    def atacar_normal(self):
        return super().atacar_normal()

    def habilidade_de_ressonancia(self):
        print(f"{self.nome} usou Dueto Seráfico...")
        energia_de_antes = self.energia
        self.energia = 0
        return self.dano_base*energia_de_antes/4


    def liberacao_de_ressonancia(self):
        print(f"{self.nome} usou Canção do Fim do Mundo...")
        return self.dano_base*200

class Noyer(PersonagemBase):
    def __init__(self):
        super().__init__(nome="Noyer", raridade="4*", elemento="Congelante", dano_base=40, taxa_crit=0.05, dano_crit=0.5, hp = 800, level = 1, energia = 0, resistencia = 1, escudo = 0)

    def atacar_normal(self):
        return super().atacar_normal()
    
    def habilidade_de_ressonancia(self):
        print(f"{self.nome} usou Parede de Gelo!")
        print(f"{self.nome} ganhou 1 escudo!")
        self.ganhar_escudo(self, 1) 
        return self.dano_base/2

    def liberacao_de_ressonancia(self):
        print(f"{self.nome} Muralha de Gelo")
        print(f"{self.nome} ganhou 4 escudos!")
        self.ganhar_escudo(self, 4)
        return self.dano_base*2

class Verina(PersonagemBase):
    def __init__(self):
        super().__init__(nome="Verina", raridade="5*", elemento="Natureza", dano_base=30, taxa_crit=0.05, dano_crit=0.5, hp = 1200, level = 1, energia = 0, resistencia = 1, escudo = 0)

    def atacar_normal(self):
        return super().atacar_normal()
    
    def habilidade_de_ressonancia(self):
        print(f"{self.nome} usou Jardinagem...")
        self.hp += 250
        return self.dano_base/2

    def liberacao_de_ressonancia(self):
        print(f"{self.nome} Árvore da Vida")
        self.hp += self.hp/50
        return self.dano_base*3

aemeath_personagem = Aemeath()
verina_personagem = Verina()
noyer_personagem = Noyer()
malerover_personagem = MaleRover()
femrover_personagem = FemRover()