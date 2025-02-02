#!/usr/bin/env python3

__version__ = "0.2.1"
__author__ = "Fábio Frade - fabiomfrade@gmail.com"
__license__ = "unlicensed"

# Imports
# import random, curses, os, time
import random
import os
import sys
from os import write
from time import sleep

import yt_dlp
from prompt_toolkit.shortcuts import clear
from youtubesearchpython import VideosSearch

# Caracteres especiais
characters = [127932, 127929, 9989, 11093]

# Variáveis obrigatórias
resp = None
download_file = "lista_download.txt"

# Funções do script
def buscar_musica(salva_arquivo=False):
    saudacao = "Digite a música que deseja baixar: " if not salva_arquivo else "Digite a música que deseja incluir na lista; Digite terminar para finalizar: "
    musica = input(saudacao)
    busca = "sair" if musica.lower() == "terminar" or musica.lower() == "sair" or not musica else VideosSearch(musica, limit=1)
    if busca == "sair":
        print()
    else:
        resultado = busca.result()
        video = resultado['result'][0]
        titulo = video['title']
        url = video['link']
        print(f"Encontrado vídeo {titulo}")
        if salva_arquivo:
            cria_lista(url)
            buscar_musica(salva_arquivo=True)
        print("Aguarde enquanto o download é feito...")
        baixar_audio(url)

def cria_lista(url):
      # Armazenando URL em arquivo de download
      with open(download_file, "a") as arquivo:
        arquivo.write(f"{url}\n")
        return None

def baixar_audio(url):
    with yt_dlp.YoutubeDL({
        'extract_audio': True,
        'format': 'bestaudio',
        'outtmpl': '%(title)s.mp3',
        'quiet': True
    }) as audio:
        info_dict = audio.extract_info(url, download = True)
        video_title = info_dict['title']
        print("MP3 baixado com sucesso\n")

# To-DO: Criar a função para baixar o vídeo ao invés do áudio apenas
def baixar_video():
    return None

def baixar_lista():
    lista = input("Digite o nome do arquivo: ")
    with open(lista, "r") as download_lista:
        for linha in download_lista.readlines():
            if linha[0:5].lower() == "https":
                print("URL encontrada, iniciando download")
                baixar_audio(linha)
            else:
                print("Detectado o nome de uma música, iniciando a busca...")
                encontra = VideosSearch(linha, limit=1)
                resultado = encontra.result()
                video = resultado['result'][0]
                url = video['link']
                baixar_audio(url)


# Dicionário de funções
opcoes = {
    "1": ("Baixar música", buscar_musica),
    "2": ("Criar e baixar uma lista", lambda: buscar_musica(salva_arquivo=True)),
    "3": ("Baixar MP3 de um Link direto", baixar_audio),
    "4": ("Baixar vídeo", baixar_video),
    "5": ("Baixar lista MP3 de um arquivo existente", baixar_lista),
}

def menu():
    print("Escolha a opção desejada: \n")
    for key, (nome, _) in opcoes.items():
        print(f"{key}. {nome}")

# Inicio do Script
print("{:^50}".format(f"Music Downloader - {__version__} - {chr(characters[random.randrange(0,2)])}"))
while True:
    menu()
    escolha = input("Digite a opção desejada ou sair para encerrar:\n")
    if escolha.lower() in {"sair", ""}:
        print("Encerrando...")
        break

    funcao = opcoes.get(escolha, (None, None))[1]

    if funcao:
        funcao()
    else:
        print("Opção inválida! Tente novamente.\n")