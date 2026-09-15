from dataclasses import dataclass

@dataclass(frozen=True, unsafe_hash=True)
class Arma3Estrelas:
    nome: str
    atributo: str  # Apenas: "Vida", "Ataque" ou "Resistencia"
    multiplicador: float  # Ex: 0.10 representa +10%
    classes_permitidas: tuple
    raridade: int = 3

def para_dict(self) -> dict:
    return {"nome": self.nome}
# --- ARMAS 3 ESTRELAS (BÔNUS DE +5% A +15%) ---

ARMA_3_ESTRELAS_LAMINA = Arma3Estrelas(
    "Lâmina de Aço Forjado", "Ataque", 0.10, ("Guerreiro", "Arqueiro")
)
ARMA_3_ESTRELAS_CAJADO = Arma3Estrelas(
    "Cajado do Aprendiz Éter", "Ataque", 0.08, ("Mago",)
)
ARMA_3_ESTRELAS_ARCO = Arma3Estrelas(
    "Arco de Salgueiro", "Ataque", 0.09, ("Arqueiro",)
)
ARMA_3_ESTRELAS_DAGA = Arma3Estrelas(
    "Daga de Cobre Afiada", "Ataque", 0.07, ("Guerreiro", "Arqueiro")
)
ARMA_3_ESTRELAS_LANCA = Arma3Estrelas(
    "Lança do Guardião", "Ataque", 0.11, ("Guerreiro",)
)
ARMA_3_ESTRELAS_MARTELO = Arma3Estrelas(
    "Martelo de Ferro Batido", "Ataque", 0.12, ("Guerreiro",)
)
ARMA_3_ESTRELAS_LIVRO = Arma3Estrelas("Livro Desgastado", "Ataque", 0.08, ("Mago",))

# EQUIPAMENTOS DE RESISTÊNCIA E VIDA
ARMA_3_ESTRELAS_ESCUDO = Arma3Estrelas(
    "Escudo de Ferro Batido", "Resistencia", 0.08, ("Guerreiro",)
)
ARMA_3_ESTRELAS_PEITORAL = Arma3Estrelas(
    "Peitoral de Couro", "Resistencia", 0.07, ("Guerreiro", "Arqueiro")
)
ARMA_3_ESTRELAS_ELMO = Arma3Estrelas(
    "Elmo de Aço Simples", "Resistencia", 0.05, ("Guerreiro",)
)
ARMA_3_ESTRELAS_MANTO = Arma3Estrelas(
    "Manto de Estudante", "Vida", 0.15, ("Mago", "Todas")
)
ARMA_3_ESTRELAS_BOTAS = Arma3Estrelas(
    "Botas de Couro", "Resistencia", 0.05, ("Todas",)
)
ARMA_3_ESTRELAS_ANEL = Arma3Estrelas("Anel de Latão", "Vida", 0.10, ("Todas",))
ARMA_3_ESTRELAS_COLAR = Arma3Estrelas("Colar do Aprendiz", "Vida", 0.12, ("Todas",))


# --- POOL UNIFICADO 3 ESTRELAS ---

POOL_3_ESTRELAS = [
    ARMA_3_ESTRELAS_LAMINA,
    ARMA_3_ESTRELAS_CAJADO,
    ARMA_3_ESTRELAS_ARCO,
    ARMA_3_ESTRELAS_DAGA,
    ARMA_3_ESTRELAS_LANCA,
    ARMA_3_ESTRELAS_MARTELO,
    ARMA_3_ESTRELAS_LIVRO,
    ARMA_3_ESTRELAS_ESCUDO,
    ARMA_3_ESTRELAS_PEITORAL,
    ARMA_3_ESTRELAS_ELMO,
    ARMA_3_ESTRELAS_MANTO,
    ARMA_3_ESTRELAS_BOTAS,
    ARMA_3_ESTRELAS_ANEL,
    ARMA_3_ESTRELAS_COLAR,
]

CATALOGO_3_ESTRELAS = {arma.nome: arma for arma in POOL_3_ESTRELAS}

def obter_arma(nome:str) -> Arma3Estrelas:
    arma = CATALOGO_3_ESTRELAS.get(nome)
    if not arma:
        raise ValueError(f"A arma não foi encontrada")
    return arma