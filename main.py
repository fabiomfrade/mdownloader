#!/usr/bin/env python3

"""
Projeto desenvolvido para fazer o download de músicas no YouTube, baseado em uma lista fornecida pelo usuário
O usuário irá inserir os nomes das músicas a serem baixadas, um por vez;
O script irá procurar o vídeo correspondente no YouTube e irá fazer o download em formato MP3

Para o futuro, o usuário poderá escolher entre baixar somente o MP3, o vídeo ou ambos
"""
__version__ = "0.1.4"
__author__ = "Fábio Frade - fabiomfrade@gmail.com"
__license__ = "unlicensed"

# Imports
import random, curses, os, time
from os import write

from pytube import YouTube
from youtubesearchpython import VideosSearch
# Caracteres especiais
characters = [127932, 127929, 9989, 11093]

# Variáveis obrigatórias
musica = []
resp = ""
download = ".download_links.tmp"

# Inicio do Script
print("{:^50}".format(f"Music Downloader - {__version__} - {chr(characters[random.randrange(0,2)])}"))

# Funções
while True:
    resp = input(f"Digite o nome da música a baixar; Digite 'sair' para encerrar: ")
    if resp.lower() == "sair" or resp == "":
        break
    else:
        busca = VideosSearch(resp, limit=1)
        resultado = busca.result()
        try:
            video = resultado['result'][0]
            titulo = video["title"]
            url = video["link"]
            print(f"Titulo: {titulo}\nURL: {url}")
            with open(download, "a") as arquivo:
                arquivo.write(f"{url}\n")
        except:
            print("Nenhum Video encontrado")