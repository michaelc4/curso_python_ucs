# coding: utf-8
import random
from jogador import Jogador

def ler_arquivo(arquivo):
    try:
        with open(arquivo, 'rt') as file:
            data = file.read()
    except IOError:
        print('não foi possivel abrir o arquivo')
    return data.split('\n')


def jogar():
    palavras = ler_arquivo('forca_python.txt')

    palavra = (random.choice(palavras)).upper()
    aPalavra = list('_' * len(palavra))

    Jogador.importar_jogadores()
    nome = (input('informe o nome do jogador ')).upper()

    counter = 0
    ntentativas = 0
    while counter < len(palavra) and ntentativas < 6:
        letra = (input('digite uma letra ')).upper()
        if letra in palavra:
            for index, l in enumerate(palavra):
                if letra == l:
                    aPalavra[index] = letra
                    counter += 1
        else:
            ntentativas += 1
        print(aPalavra)

    if ntentativas >= 6:
        print('Enforcado')
    else:
        print('Ganhou')
        jogador = Jogador.buscar_jogador(nome)
        if jogador != None:
            jogador.pontuacao += 1
        else:
            Jogador(nome, 1)

    Jogador.salvar_jogadores()
