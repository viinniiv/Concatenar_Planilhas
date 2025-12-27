# Concatenar_Planilhas
Este script concatena todos os arquivos de dados (.csv e .xlsx) de uma pasta de entrada em um único arquivo .csv final, salvo em uma pasta de saída especificada pelo usuário.

O script:

  - Solicita o caminho da pasta de entrada (onde estão os arquivos .csv e .xlsx).
  - Verifica se a pasta existe.
  - Solicita o caminho da pasta de saída (onde o arquivo final será salvo).
  - Cria a pasta de saída, caso não exista (com confirmação do usuário).
  - Solicita o nome do arquivo de saída (ex.: Completao.csv).
  - Lê todos os arquivos .csv e .xlsx da pasta de entrada.
  - Concatena todos os DataFrames.
  - Salva o resultado em um único arquivo .csv com separador ;.

## Dependências

O script utiliza as seguintes bibliotecas Python:

  - pandas 
  - openpyxl (usado pelo pandas para leitura de arquivos .xlsx)

## Instalação das dependências

Antes de executar o script, instale as dependências com:

    pip install pandas openpyxl  

## Executando:
    python concatena_arquivos.py  

Informe:

  - O caminho da pasta de entrada (onde estão os .csv/.xlsx).
  - O caminho da pasta de saída.
  - O nome do arquivo final (por exemplo: Completao.csv).

O script então irá gerar um único arquivo .csv com todos os dados concatenados.
