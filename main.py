#!/usr/bin/env python3

"""
Projeto desenvolvido para fazer o download de músicas no YouTube, baseado em uma lista fornecida pelo usuário
O usuário irá inserir os nomes das músicas a serem baixadas, um por vez;
O script irá procurar o vídeo correspondente no YouTube e irá fazer o download em formato MP3

Para o futuro, o usuário poderá escolher entre baixar somente o MP3, o vídeo ou ambos
"""
__version__ = "0.1.0"
__author__ = "Fábio Frade - fabiomfrade@gmail.com"
__license__ = "unlicensed"

# Imports
import random, curses, os, time
from pytube import YouTube
from youtubesearchpython import VideosSearch
# Caracteres especiais
characters = [127932, 127929, 9989, 11093]

# Variáveis obrigatórias
musica = []
resp = ""


# Inicio do Script
print("{:^50}".format(f"Music Downloader - v_0.1.0 - {chr(characters[random.randrange(0,2)])}"))

# Funções
while resp != 'sair':
    print(f"Digite o nome da música a baixar; Digite 'sair' para encerrar: ")
    resp = input()

    if resp != 'sair':
        musica.append(resp)

    videosSearch = VideosSearch(resp, limit=2)
    resultado = dict(videosSearch.result())
    # print(videosSearch.result())
    for chave, valor in resultado.items():
        print(f"{chave}, {valor}\n")