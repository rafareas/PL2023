import re
import json

def creat_dict():
    dados = []
    with open('processos.txt','r') as processos:
        for linhas in processos:
            if linhas.strip():
                # faz o split de uma linha e guarda em linhas
                valores = linhas.strip().split(',')
                mystring = " ".join(valores)
                dados.append(mystring)

    proc = re.compile(r'(?P<pasta>\d+)::(?P<ano>\d+)-(?P<mes>\d+)-(?P<dia>\d+)::(?P<nome>[\w+ ]+)::(?P<nomePai>[\w+ ]+)::(?P<nomeMae>[\w+ ]+)::(?P<parentes>[^:]*)::')

    processos = []
    for i in dados:
        match = proc.match(i)
        if match:
            processos.append(match.groupdict())

    print(processos)
    return processos

# a) Calcula a frequência de processos por ano (primeiro elemento da data);
def freq_proc_ano(processos):
    freq = {}
    for anos in processos:
        if anos["ano"] not in freq:
            freq[anos["ano"]] = 0 #adiciona os anos a 0 nas frequencias
        if anos["ano"] in freq:
            freq[anos["ano"]] += 1

    print(freq)
    return freq

# b) Calcula a frequência de nomes próprios (o primeiro em cada nome) e apelidos (o ultimo em cada nome) por séculos e apresenta os 5 mais usados;
def freq_nome_sobrenome(processos):
    # definir um dicionário para armazenar as frequências dos nomes por século
    nomes_por_seculo = {f'Século {i}': {'Nome': {}, 'Sobrenome': {}} for i in range(17, 21)}

    # iterar sobre cada registro do conjunto de dados
    for nome in processos:
        # extrair o primeiro e último nomes utilizando expressões regulares
        primeiro_nome = re.search(r'^\w+', nome["nome"])[0]
        ultimo_nome = re.search(r'\w+$', nome["nome"])[0]

        # determinar o século a partir do ano de nascimento
        ano_nascimento = int(re.findall(r'\b\d{4}\b', nome["ano"])[0])
        seculo = (ano_nascimento - 1) // 100 + 1

        # incrementar a contagem dos nomes próprios e apelidos no dicionário
        nomes_por_seculo[f'Século {seculo}']['Nome'][primeiro_nome] = nomes_por_seculo[f'Século {seculo}']['Nome'].get(primeiro_nome, 0) + 1
        nomes_por_seculo[f'Século {seculo}']['Sobrenome'][ultimo_nome] = nomes_por_seculo[f'Século {seculo}']['Sobrenome'].get(ultimo_nome, 0) + 1

    # imprimir os 5 nomes próprios e apelidos mais comuns por século
    for seculo, nomes_freqs in nomes_por_seculo.items():
        print(f'{seculo}:')
        print('  Nome:')
        for nome, freq in sorted(nomes_freqs['Nome'].items(), key=lambda x: x[1], reverse=True)[:5]:
            print(f'    {nome}: {freq}')
        print('  Sobrenome:')
        for nome, freq in sorted(nomes_freqs['Sobrenome'].items(), key=lambda x: x[1], reverse=True)[:5]:
            print(f'    {nome}: {freq}')

# c) Calcula a frequência dos vários tipos de relação: irmão, sobrinho, etc.;
def freq_relation(processos):
    re_formula = re.compile(r"::(.*?)::")
    relacoes = {"irmão": 0, "tio": 0, "sobrinho": 0}
    dados = []
    for proc in processos:
        dados.append(proc["parentes"])
    lista_sem_vazios = list(filter(bool, dados))

    for texto in lista_sem_vazios:
        if re.search(r'\bIrmao\b', texto):
            relacoes["irmão"] += 1
        if re.search(r'\bTio\b', texto):
            relacoes["tio"] += 1
        if re.search(r'\bSobrinho\b', texto):
            relacoes["sobrinho"] += 1

    print(relacoes)
    return relacoes

# d) Converta os 20 primeiros registos num novo ficheiro de output mas em formato Json.
def escrever_json():
    with open('processos.txt', 'r') as arquivo:
        dados = []
        for i in range(20):
            linha = arquivo.readline().strip()
            if linha:
                dados.append(linha)

    with open('output.json', 'w') as output:
        json.dump(dados, output)

def main():
    processos = creat_dict()
    freq_ano = freq_proc_ano(processos)
    freq_nome = freq_nome_sobrenome(processos)
    freq_relacao = freq_relation(processos)
    em_json = escrever_json()


if __name__ == "__main__":
    main()
