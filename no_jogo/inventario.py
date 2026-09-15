import json
from rich.console import Console
from rich.table import Table

console = Console()
def exibir_inventario(player):
    dados = {}
    with open("usuarios.json", 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
    tabela_inventario = Table(title="Inventário do Jogador:")
    tabela_inventario.add_column("Item", style="bold purple")
    tabela_inventario.add_column("Equipado por", style="bold")
    dados_do_inventario = dados[player.nome]["Inventário"]
    for chav, val in dados_do_inventario.items():
        if isinstance(val, dict):
            formatado = ", ".join(val.keys())
        else:
            formatado = str(val)
        tabela_inventario.add_row(chav, formatado)
        console.print(tabela_inventario)