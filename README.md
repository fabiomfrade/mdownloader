# Music Downloader

Music Downloader é um script em Python para buscar, baixar e organizar músicas e vídeos diretamente do YouTube.

## Objetivo

O objetivo deste projeto é permitir o download de músicas extraídas de vídeos do YouTube e permitir que o usuário 
decida entre baixar vídeos ou apenas o áudio.

## Propósito

O propósito deste projeto é meramente educacional. Enquanto aprimoro conhecimentos da linguagem Python, vou melhorando o código criado aqui e mantendo as versões anteriores em histórico de commits e/ou tags do projeto.

## Recursos

- Buscar e baixar músicas individualmente.
- Criar listas de músicas para downloads em lote.
- Baixar vídeos completos em formato MP4.
- Suporte a downloads tanto por nomes de músicas quanto URLs diretas.

## Requisitos

Certifique-se de ter instalado:

- Python 3.6 ou superior
- As bibliotecas Python:
  - yt-dlp
  - prompt_toolkit
  - youtube-search-python
  - ffmpeg
- O pacote `ffmpeg` instalado no sistema operacional

Para instalar as dependências Python, execute:

```bash
pip install -f requirements.txt
```

Para instalar o pacote `ffmpeg` em distribuições baseadas em Debian:

```bash
sudo apt-get install ffmpeg
```

## Como Usar

### Execução

Para iniciar o script, basta rodar o comando:

```bash
python3 main.py
```

### Menu de Opções

1. **Baixar música**: Informe o nome da música desejada para o download.
2. **Criar e baixar uma lista**: Adicione diversas músicas para um download em lote.
3. **Baixar MP3 de um link direto**: Insira a URL de um vídeo do YouTube para extrair o áudio.
4. **Baixar vídeo**: Informe o nome de um vídeo para fazer download completo.
5. **Baixar lista MP3 de um arquivo existente**: Forneça o caminho para um arquivo contendo URLs ou nomes de músicas.

## Estrutura de Saída

- Arquivos MP3 serão salvos no diretório `mp3/`.
- Vídeos serão salvos no diretório `videos/`.

## Exemplo de Uso

### Download Individual de uma Música

```bash
Digite a opção desejada ou sair para encerrar:
1
Digite a música que deseja baixar: Nome da Música
```

### Criação de Lista

```bash
Digite a opção desejada ou sair para encerrar:
2
Digite a música que deseja incluir na lista; Digite terminar para finalizar: Música 1
Digite a música que deseja incluir na lista; Digite terminar para finalizar: terminar
```

## Considerações Legais

Este projeto não armazena conteúdo protegido por direitos autorais. Todo o material baixado é de responsabilidade exclusiva do usuário. Os direitos autorais pertencem ao YouTube e aos seus respectivos criadores.

## Status do Projeto

Este projeto está em desenvolvimento ativo. Novas funcionalidades devem ser adicionadas e o README pode ser alterado a qualquer momento para refletir essas mudanças.

## Licença

Este projeto está sob a licença `unlicensed`.

## Autor

Fábio Frade - [fabiomfrade@gmail.com](mailto:fabiomfrade@gmail.com)

