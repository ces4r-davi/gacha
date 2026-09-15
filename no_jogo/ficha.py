import json
from rich.console import Console
from rich.table import Table

console = Console()
def exibir_ficha(player):
    dados = {}
    with open("usuarios.json", 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
    tabela_jogador = Table(title="Dados do Jogador:")
    tabela_jogador.add_column("Informação", style="bold purple")
    tabela_jogador.add_column("Valor", style="bold")
    dados_do_jogador = dados[player.nome]
    for chav, val in dados_do_jogador.items():
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