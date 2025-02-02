# Music Downloader - mdownloader
Programa feito para baixar músicas do YouTube, atualmente em formato MP3 de máxima qualidade.

## Objetivo
O objetivo deste projeto é permitir o download de músicas extraídas de vídeos do YouTube e em futuras versões, permitir que o usuário decida entre baixar vídeos ou apenas o áudio, como é o objetivo inicial. 
### Propósito
O propósito deste projeto é meramente educacional. Enquanto aprimoro conhecimentos da linguagem Python, vou melhorando o código criado aqui e mantendo as versões anteriores em histórico de ``commits`` e/ou ``tags`` do projeto.

### Funções finalizadas
  * Buscar Música
    * Pede ao usuário para informar a música que deseja baixar e esta função irá encontrar o vídeo correspondente, extrair a URL e passar para a próxima função
  * Baixar Áudio
    * Recebe a URL do vídeo encontrado, extrai apenas o áudio e faz o download do mesmo em formato MP3 de alta qualidade
  * Criar Lista
    * Instrui o usuário a inserir nomes de músicas a serem baixadas e ao digitar ___"terminar"___, o sistema baixa a lista de músicas informadas em formato ```MP3```
  * Baixar Lista existente
    * Esta função permite que você indique uma lista contendo ou o link do vídeo a ser baixado, ou o nome da música que deseja baixar;
    * Caso seja uma URL, o download do MP3 se inicia imediatamente, caso contrário, primeiro será feita uma busca pelo vídeo e então o áudio será extraído.
  * Baixar vídeo
    * Esta função permite que você diga qual o nome do vídeo que deseja baixar; Ela irá buscar o vídeo e fazer o download do mesmo em um diretório chamado vídeos
---
## Copyrights mantidos pelos donos dos vídeos pesquisados
### ___Este projeto está sendo desenvolvido e este README tende a mudar constantemente com a evolução do projeto___