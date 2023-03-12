import re
import json
import csv


def csv_to_json():
    with open("alunos.csv", 'r') as csv_file:
        # Ler a primeira linha para obter os nomes das colunas
        colunas = csv_file.readline().strip().split(',')
        # Criar uma lista vazia para armazenar os dados
        dados = []
        # Iterar sobre as linhas restantes do arquivo
        for linha in csv_file:
            # Separar os campos da linha pelo caractere separador
            campos = linha.strip().split(',')
            # Criar um dicionário com os dados da linha
            dicionario = {}
            for i in range(len(colunas)):
                dicionario[colunas[i]] = campos[i]
            # Adicionar o dicionário à lista de dados
            dados.append(dicionario)
    # Converter a lista de dados para JSON e escrever em um arquivo
    with open("alunos.json", 'w') as json_file:
        json_file.write(json.dumps(dados, indent=2))


# Listas:
def lista_json():
    dados = []
    with open("alunos2.csv",'r',newline='') as csv_file:
        identificador_semAlt = csv_file.readline().strip().split(',')
        identificador = [elem for elem in identificador_semAlt if bool(elem)] # retira as strings vazias

        regex = re.compile(r'(\s*\w+)\{(\d+)\}')

        for linha in csv_file:
            if linha.strip():
                dicionario = {} # cria um novo dicionário para cada linha do arquivo
                sep = linha.strip().split(',')
                count = 0
                for i in identificador:
                    match = regex.search(i)
                    if not match:
                        dicionario[i] = sep[count]
                        count += 1
                    else:
                        tmp = count
                        lista = []
                        for num in range(int(match.group(2))):
                            lista.append(sep[tmp])
                            tmp += 1
                        dicionario[match.group(1)] = lista
                dados.append(dicionario)
        with open("alunos2.json", "w") as json_file:
            json.dump(dados, json_file, indent=2)


# Listas com um intervalo de tamanhos
def list_intervalo():
    dados = []
    with open("alunos3.csv", 'r', newline='') as csv_file:
        linha = csv_file.readline().strip()
        identificador= re.findall(r'[^,{]*{[^}]*}[^,]*|[^,]+', linha)

        regex = re.compile(r'(\s*\w+)\{(\d+),(\d+)\}')

        for linha in csv_file:
            if linha.strip():
                dicionario = {}
                sep = linha.strip().split(',')
                count = 0
                for i in identificador:
                    match = regex.search(i)
                    if not match:
                        dicionario[i] = sep[count]
                        count += 1
                    else:
                        tmp = count
                        lista = []
                        for num in range(int(match.group(2)), int(match.group(3)) + 1):
                            lista.append(sep[tmp])
                            tmp += 1
                        dicionario[match.group(1)] = lista
                dados.append(dicionario)
        with open("alunos3.json", "w") as json_file:
            json.dump(dados, json_file, indent=2)


# Funções de agregação

def list_agregacao():
    dados = []
    with open("alunos4.csv", 'r', newline='') as csv_file:
        linha = csv_file.readline().strip()
        identificador= re.findall(r'[^,{]*{[^}]*}[^,]*|[^,]+', linha)

        regex = re.compile(r'(\s*\w+)\{(\d+),(\d+)\}::(\w+)')

        for linha in csv_file:
            if linha.strip():
                dicionario = {}
                sep = linha.strip().split(',')
                count = 0
                for i in identificador:
                    match = regex.search(i)
                    if not match:
                        dicionario[i] = sep[count]
                        count += 1
                    else:
                        tmp = count
                        lista = []
                        for num in range(int(match.group(2)), int(match.group(3)) + 1):
                            lista.append(sep[tmp])
                            tmp += 1
                        if match.group(4) == 'sum':
                            dicionario[match.group(1)] = sum(map(int, lista))
                        elif match.group(4) == 'media':
                            dicionario[match.group(1)] = sum(map(int, lista)) / len(lista)
                dados.append(dicionario)

        with open("alunos4.json", "w") as json_file:
            json.dump(dados, json_file, indent=2)


def main():
    csv_to_json()
    lista_json()
    list_intervalo()
    list_agregacao()

if __name__ == "__main__":
    main()
