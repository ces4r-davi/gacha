import os

RESPOSTAS_SIM = {
    "sim", "s", "y", "yes", "ss", "si", "com certeza", "comcerteza", "bora", 
    "partiu", "claro", "certeza", "manda", "manda ver", "pode ser", "fechado", 
    "dale", "vai", "bora la", "borala", "obvio", "com ctz", "ctz", "1", 
    "true", "ok", "k", "oky", "okay"
}

RESPOSTAS_NAO = {
    "não", "nao", "n", "no", "nn", "nop", "nope", "nem", "nunca", 
    "de jeito nenhum", "jamais", "deixa", "deixa pra la", "deixaprala", 
    "agora nao", "agora não", "passo", "cancelar", "cancela", "sair", 
    "stop", "0", "false"
}

def limpar_tela():
    os.system('cls')