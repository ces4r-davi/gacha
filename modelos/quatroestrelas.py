from dataclasses import dataclass
from modelos.personagens import noyer_personagem

@dataclass(frozen=True)
class Arma4Estrelas:
    nome: str
    atributo: str
    qntdatributo: float
    classes_permitidas: tuple
    raridade: int=4

def para_dict(self) -> dict:
    return {"nome": self.nome}

ARMA_4_ESTRELAS_LAMINA = Arma4Estrelas(
    "Espada de Aço Forjado Real", "Ataque", 0.25, ("Guerreiro",)
)
ARMA_4_ESTRELAS_CAJADO = Arma4Estrelas(
    "Cajado do Arcanista", "Ataque", 0.22, ("Mago",)
)
ARMA_4_ESTRELAS_ARCO = Arma4Estrelas(
    "Arco de Caçador Ébano", "Ataque", 0.24, ("Arqueiro",)
)
ARMA_4_ESTRELAS_DAGA = Arma4Estrelas(
    "Adaga de Prata Sombria", "Ataque", 0.20, ("Guerreiro", "Arqueiro")
)
ARMA_4_ESTRELAS_LANCA = Arma4Estrelas(
    "Lança do Cavaleiro de Elite", "Ataque", 0.28, ("Guerreiro",)
)
ARMA_4_ESTRELAS_MARTELO = Arma4Estrelas(
    "Martelo de Guerra de Milício", "Ataque", 0.30, ("Guerreiro",)
)
ARMA_4_ESTRELAS_LIVRO = Arma4Estrelas(
    "Grimório de Runas Antigas", "Ataque", 0.21, ("Mago",)
)

# EQUIPAMENTOS DE RESISTÊNCIA E VIDA
ARMA_4_ESTRELAS_ESCUDO = Arma4Estrelas(
    "Escudo da Guarda Real", "Resistencia", 0.20, ("Guerreiro",)
)
ARMA_4_ESTRELAS_PEITORAL = Arma4Estrelas(
    "Peitoral de Malha Reforçado", "Resistencia", 0.18, ("Guerreiro", "Arqueiro")
)
ARMA_4_ESTRELAS_ELMO = Arma4Estrelas(
    "Elmo de Aço Escuro", "Resistencia", 0.15, ("Guerreiro",)
)
ARMA_4_ESTRELAS_MANTO = Arma4Estrelas(
    "Manto de Tecido Éter", "Vida", 0.35, ("Mago", "Todas")
)
ARMA_4_ESTRELAS_BOTAS = Arma4Estrelas(
    "Botas do Rastreador", "Resistencia", 0.12, ("Todas",)
)
ARMA_4_ESTRELAS_ANEL = Arma4Estrelas(
    "Anel de Prata Encantado", "Vida", 0.25, ("Todas",)
)
ARMA_4_ESTRELAS_COLAR = Arma4Estrelas(
    "Colar de Quartzo Protetor", "Vida", 0.30, ("Todas",)
)


# --- POOL UNIFICADO 4 ESTRELAS ---

POOL_4_ESTRELAS = [
    ARMA_4_ESTRELAS_LAMINA,
    ARMA_4_ESTRELAS_CAJADO,
    ARMA_4_ESTRELAS_ARCO,
    ARMA_4_ESTRELAS_DAGA,
    ARMA_4_ESTRELAS_LANCA,
    ARMA_4_ESTRELAS_MARTELO,
    ARMA_4_ESTRELAS_LIVRO,
    ARMA_4_ESTRELAS_ESCUDO,
    ARMA_4_ESTRELAS_PEITORAL,
    ARMA_4_ESTRELAS_ELMO,
    ARMA_4_ESTRELAS_MANTO,
    ARMA_4_ESTRELAS_BOTAS,
    ARMA_4_ESTRELAS_ANEL,
    ARMA_4_ESTRELAS_COLAR,
]
POOL_4_ESTRELAS_PERSONAGENS = [
    noyer_personagem,
]

catalogo_armas_4estrelas = {arma.nome:arma for arma in POOL_4_ESTRELAS}
catalogo_personagens_4estrelas = {personagem.nome:personagem for personagem in POOL_4_ESTRELAS_PERSONAGENS}

def obter_arma(nome:str) -> Arma4Estrelas:
    arma = catalogo_armas_4estrelas.get(nome)
    if not arma:
        raise ValueError("Arma não encontrada.")
    return arma

def obter_personagem(nome:str):
    personagem = catalogo_personagens_4estrelas.get(nome)
    if not personagem:
        raise ValueError("Personagem não encontrado.")
    return personagem