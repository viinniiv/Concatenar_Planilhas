import os
import pandas as pd

def main():
    data_arquivo_folder = input("Digite o caminho da pasta de ENTRADA (onde estão os .csv/.xlsx): ").strip()        
    
    
    if not os.path.isdir(data_arquivo_folder):
        print(f"Erro: A pasta de entrada '{data_arquivo_folder}' não existe.")
        return
    
    output_folder = input("Digite o caminho da pasta de SAÍDA (onde será salvo o arquivo final): ").strip()
        
    if not os.path.isdir(output_folder):
        criar = input(f"A pasta '{output_folder}' não existe. Deseja criá-la? (s/n): ").strip().lower()
        if criar == 's':
            os.makedirs(output_folder, exist_ok=True)
            print(f"Pasta '{output_folder}' criada.")
        else:
            print("Encerrando o script, pois a pasta de saída não existe.")
            return
    
    output_filename = input("Digite o NOME do arquivo de saída (ex: Completao.csv): ").strip()
    if not output_filename.lower().endswith('.csv'):
        output_filename += '.csv'

    dfs = []
    for file in os.listdir(data_arquivo_folder):
        file_lower = file.lower()
        if file_lower.endswith('.csv') or file_lower.endswith('.xlsx'):
            filepath = os.path.join(data_arquivo_folder, file)
            print(f"Carregando arquivo {filepath}...")

            try:
                if file_lower.endswith('.csv'):
                    df = pd.read_csv(filepath, sep=';')
                else:                      
                    df = pd.read_excel(filepath)
                dfs.append(df)
            except Exception as e:
                print(f"Erro ao carregar '{filepath}': {e}")

    if not dfs:
        print("Nenhum arquivo .csv ou .xlsx encontrado na pasta de entrada.")
        return

    print(f"Total de arquivos carregados: {len(dfs)}")

    df_principal = pd.concat(dfs, axis=0, ignore_index=True)
    output_path = os.path.join(output_folder, output_filename)
    
    df_principal.to_csv(output_path, index=False, sep=';')
    print(f"Arquivo final salvo em: {output_path}")

if __name__ == "__main__":
    main()