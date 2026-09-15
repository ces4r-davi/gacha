from rich import print
import random

def cara_ou_coroa(player):
    print("[bold cyan]=== BEM-VINDO AO CARA OU COROA (CASSINO) ===[/bold cyan]\n")
    print("[bold yellow]REGRAS DO JOGO:[/bold yellow]")
    print("1. [bold]Aposta Mínima:[/bold] 100 gemas.")
    
    print("[bold white]3. Multiplicadores de Vitória:[/bold white]")
    print("   • [bold green]Apostas Normais (< 1000 gemas):[/bold green]")
    print("     - [cyan]Cara:[/cyan] Ganho de [bold green]2.1x[/bold green] a aposta, porém perda de 1.2x.")
    print("     - [magenta]Coroa:[/magenta] Ganho de [bold green]1.8x[/bold green] a aposta.")
    
    print("   • [bold green]Apostas High Roller (≥ 1000 gemas):[/bold green]")
    print("     - [cyan]Cara:[/cyan] Ganho de [bold green]1.8x[/bold green] a aposta.")
    print("     - [yellow]Coroa:[/yellow] Ganho de [bold green]3.5x[/bold green] a aposta, porém perda de 1.5x\n")
    print("4. [bold bold_breeze]Cair em pé:[/bold bold_breeze] A moeda pode cair em [bold yellow]PÉ[/bold yellow]! Se isso acontecer, você ganha um super multiplicador de [bold yellow]100x[/bold yellow] o valor apostado!\n")
    
    print("5. [bold red]Perda:[/bold red] Em caso de derrota, você perde [bold red]100%[/bold red] do valor apostado (1x).\n")
    while True:
        opcoes = ["jogador", "banca", "em_pe"]
        probabilidades = [44.95, 54.95, 0.1]
        
        resultado = random.choices(opcoes,  weights=probabilidades, k=1)[0]

        print("O que você deseja?:")
        print("1 - Apostar em Cara")
        print("2 - Apostar em Coroa")
        print("0 - Sair")
        try:
            escolha = int(input("Digite a opção --> "))
            if escolha > 2 or escolha < 0:
                print("Digite um número válido!")
                continue
        except ValueError as e:
            print("Digite apenas valores válidos!")
            continue
        multiplicador_de_ganho = 1
        multiplicador_de_perda = 1
        if escolha == 0:
            return
        try:
            quantia = int(input("Digite a quantidade que deseja apostar --> "))
            if quantia < 0 or quantia > player.gemas:
                print("Digite um valor que você tenha em saldo!")
                continue
        except ValueError as e:
                print("Digite apenas valores válidos!")
                continue

        escolha_nome = ""
        escolha_contraria_nome = ""

        if escolha == 1:
            escolha_nome = "Cara"
            escolha_contraria_nome = "Coroa"
            if quantia < 1000:
                multiplicador_deP_ganho = 2.1
                multiplicador_de_perda = 1.2
            else:
                multiplicador_de_ganho = 1.8
        elif escolha == 2:
            escolha_nome = "Coroa"
            escolha_contraria_nome = "Cara"
            if quantia < 1000:
                multiplicador_de_ganho = 3.5
                multiplicador_de_perda = 1.5
            else:
                multiplicador_de_ganho = 1.8


        if resultado == "jogador":
            ganho = quantia*multiplicador_de_ganho
            print(f"Caiu {escolha_nome}!")
            print(f"Você recebeu {ganho} gemas!")
            player.gemas += ganho
        elif resultado == "banca":
            perda = quantia*multiplicador_de_perda
            print(f"Caiu {escolha_contraria_nome}...")
            print(f"Você perdeu {perda} gemas.")
            player.gemas -= perda
        elif resultado == "em_pe":
            ganho = quantia*100
            print("A moeda caiu em pé!!")
            print(f"Você tirou a sorte grande, ganhou {ganho} gemas!!!!")
            player.gemas += ganho