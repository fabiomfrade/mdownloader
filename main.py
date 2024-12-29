#!/usr/bin/env python3

__version__ = "0.2.0"
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
resp = None
# download = ".download_links.tmp"

# Funções do script
def buscar_video(musica):
    busca = VideosSearch(musica, limit=1)
    resultado = busca.result()
    video = resultado['result'][0]
    titulo = video['title']
    url = video['link']
    print(f"Encontrado vídeo {titulo}")
    print("Aguarde enquanto o download é feito...")
    baixar_audio(url)
#   # Armazenando URL em arquivo temporário
#   with open(download, "a") as arquivo:
#   arquivo.write(f"{url}\n")

def baixar_audio(url):
    with yt_dlp.YoutubeDL({'extract_audio': True, 'format': 'bestaudio', 'outtmpl': '%(title)s.mp3', 'quiet': True}) as audio:
        info_dict = audio.extract_info(url, download = True)
        video_title = info_dict['title']
        print("MP3 baixado com sucesso\n")


# Inicio do Script
print("{:^50}".format(f"Music Downloader - {__version__} - {chr(characters[random.randrange(0,2)])}"))
while True:
    resp = input(f"Digite o nome da música a baixar\nDigite 'sair' para encerrar: ")
    if resp.lower() == "sair" or not resp:
        sys.exit(0)
    else:
        buscar_video(resp)


