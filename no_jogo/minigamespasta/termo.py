from no_jogo.minigamespasta.palavras import DICIONARIO_5_LETRAS
import random
from rich import print

def termo(player):
    recompensa = 200
    print("[bold dark_green]======BEM VINDO AO TERMO!======[/]")
    print("[bold blue]Regras:[/]")
    palavra, significado = random.choice(list(DICIONARIO_5_LETRAS.items()))
    tentativa = ""
    palavra_criptografada = list("*****")
    print(palavra)
    letras_erradas = []
    tentativas_totais = 0
    string_criptografada = "".join(palavra_criptografada)
    print(string_criptografada)

    while tentativa != palavra:
        tentativas_totais +=1
        if tentativas_totais > 5:
            print("Você não conseguiu descobrir a palavra de hoje, boa sorte na próxima!")
            print(f"A palavra era:\n{palavra}: {significado}")
            return

        try:
            tentativa = input("Digite a palavra de 5 letras: ")
            tentativa = tentativa.upper()
        except ValueError:
            print("Digite uma palavra válida!")
        if tentativa == palavra:
            break

        if len(tentativa) != 5:
            print("A palavra precisa ter 5 letras!")
            continue

        for indice, letra in enumerate(tentativa):
            if palavra[indice] == tentativa[indice]:
                palavra_criptografada[indice] = f"[bold green]{letra}[/bold green]"
            elif letra in palavra:
                palavra_criptografada[indice] = f"[bold yellow]{letra}[/bold yellow]"
            elif letra not in letras_erradas:
                letras_erradas.append(letra)

        string_criptografada = "".join(palavra_criptografada)
        print(string_criptografada)
        print(f"Letras [bold red]ERRADAS[/]: {letras_erradas}\n")
        if tentativas_totais >3:
            try:
                dica = input("Deseja obter uma dica?(Diminui a recompensa em 30%)[S/N] --> ").lower()
            except ValueError:
                print("Digite um valor válido!")
            if dica == 's':
                print(f"Dica: {significado}")
                recompensa = 140

    print("Você descobriu a palavra!\n")
    print(f"Numero de tentativas: {tentativas_totais}")
    print(f"{palavra}: {significado}")
    player.gemas+=recompensa