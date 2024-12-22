#!/usr/bin/env python3

"""
Projeto desenvolvido para fazer o download de músicas no YouTube, baseado em uma lista fornecida pelo usuário
O usuário irá inserir os nomes das músicas a serem baixadas, um por vez;
O script irá procurar o vídeo correspondente no YouTube e irá fazer o download em formato MP3

Para o futuro, o usuário poderá escolher entre baixar somente o MP3, o vídeo ou ambos
"""
__version__ = "0.1.5"
__author__ = "Fábio Frade - fabiomfrade@gmail.com"
__license__ = "unlicensed"

# Imports
import random, curses, os, time
import sys
from os import write
import yt_dlp
from youtubesearchpython import VideosSearch
# Caracteres especiais
characters = [127932, 127929, 9989, 11093]

# Variáveis obrigatórias
resp = ""
download = ".download_links.tmp"

# Inicio do Script
print("{:^50}".format(f"Music Downloader - {__version__} - {chr(characters[random.randrange(0,2)])}"))

# Funções
# TODO: Criar funções main, de criação de lista e de download da list
while True:
    # TODO: Melhorar a validação de digitação e incluir outras opções, como download
    resp = input(f"Digite o nome da música a baixar; Digite 'sair' para encerrar: ")
    if resp.lower() == "sair" or resp == "":
        break
    else:
        busca = VideosSearch(resp, limit=1)
        resultado = busca.result()
        try:
            # Obtendo valores do vídeo encontrado
            video = resultado['result'][0]
            titulo = video["title"]
            url = video["link"]
            print(f"Titulo: {titulo}\nURL: {url}")
            # Armazenando URL em arquivo temporário
            with open(download, "a") as arquivo:
                arquivo.write(f"{url}\n")
            # Baixando o MP3
            with yt_dlp.YoutubeDL({'extract_audio': True, 'format': 'bestaudio', 'outtmpl': '%(title)s.mp3'}) as audio:
                info_dict = audio.extract_info(url, download = True)
                video_title = info_dict['title']
        except:
            print("Nenhum Video encontrado")
            sys.exit(1)