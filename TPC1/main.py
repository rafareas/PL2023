
def doenc_por_sexo(dados):

    por_sexo = {'Masculino':{'total' : 0 ,'doentes' : 0 , 'porcentagem' : 0},'Feminino':{'total' : 0 ,'doentes' : 0 , 'porcentagem' : 0}}

    for linha in range(len(dados)):
        if "M" in dados[linha]['sexo']:
            por_sexo['Masculino']['total'] += 1
            if "1" in dados[linha]['temDoenca']:
                por_sexo['Masculino']['doentes'] += 1
        if "F" in dados[linha]['sexo']:
            por_sexo['Feminino']['total'] += 1
            if "1" in dados[linha]['temDoenca']:
                por_sexo['Feminino']['doentes'] += 1

    porcentagem_M = (por_sexo['Masculino']['doentes']/por_sexo['Masculino']['total']) * 100
    porcentagem_F = (por_sexo['Feminino']['doentes']/por_sexo['Feminino']['total']) * 100
    por_sexo['Masculino']['Porcentagem'] = round(porcentagem_M,2)
    por_sexo['Feminino']['Porcentagem'] = round(porcentagem_F,2)

    return por_sexo

def tabela_doenc_por_sexo(dados):

    por_sexo = doenc_por_sexo(dados)

    header = f"{'Sexo':<20}{'Total':<10}{'Doentes':<10}{'Porcentagem':<10}\n"

    lines = []
    for col, d in por_sexo.items():
        if col == 'Masculino':
            line = f"{col:<21}{d['total']:<11}{d['doentes']:<10}{d['porcentagem']:>2}\n"
            lines.append(line)
        if col == 'Feminino':
            line = f"{col:<21}{d['total']:<11}{d['doentes']:<11}{d['porcentagem']:<10}\n"
            lines.append(line)

    table = header + ''.join(lines)
    return table

def min_max(tipo,dados):
    lista = []
    for linhas in range(len(dados)):
        lista.append(int(dados[linhas].get(tipo)))

    minimo = min(lista)
    maximo = max(lista)

    return minimo,maximo

def doenc_escalao_etario(dados):

    idade_inf, idade_sup = min_max("idade",dados)

    etaria = {}
    for i in range(idade_inf,idade_sup,4):
        etaria[i] = {'doentes' : 0}

    for linha in range(len(dados)):
        idd_doente = dados[linha]["temDoenca"]
        if idd_doente == '1':
            val_idd = dados[linha].get("idade")
            for idd in etaria.keys():
                if int(val_idd) in range(idd,idd+5):
                    etaria[idd]['doentes'] += 1

    return etaria

def tabela_doenc_escalao_etario(dados):

    etaria = doenc_escalao_etario(dados)

    header = f"{'Escalao Etario':<30}{'Doentes':>10}\n"

    lines = []
    for col, d in etaria.items():
        line = f"{col} a {col+4:<23}{d['doentes']:>10}\n"
        lines.append(line)


    table = header + ''.join(lines)

    return table

def doenc_nivel_colesterol(dados):
    col_inf,col_sup = min_max("colesterol",dados)

    doenc_por_col = {}
    for i in range(col_inf,col_sup,10):
        doenc_por_col[i] = {'doentes' : 0}

    for linha in range(len(dados)):
        doente = dados[linha]["temDoenca"]
        if doente == '1':
            val_col = dados[linha].get("colesterol")
            for col in doenc_por_col.keys():
                if int(val_col) in range(col,col+11):
                    doenc_por_col[col]['doentes'] += 1


    for col in list(doenc_por_col.keys()):
        if doenc_por_col[col]['doentes'] == 0:
            del doenc_por_col[col]

    #new_doenc_por_col = {}
    #for col in doenc_por_col:
    #    new_col = (col, col+10)
    #    new_doenc_por_col[new_col] = doenc_por_col[col]

    return doenc_por_col

def tabela_doenc_nivel_colesterol(dados):

    doenc_por_col = doenc_nivel_colesterol(dados)

    header = f"{'Intervalo de colesterol':<30}{'Doentes':>10}\n"

    lines = []
    for col, d in doenc_por_col.items():
        line = f"{col} a {col+10:<23}{d['doentes']:>10}\n"
        lines.append(line)


    table = header + ''.join(lines)
    return table

def get_dados_csv():
    dados = []
    with open('myheart.csv','r') as myheart:
        #utilizado o método strip para tirar os espaçoes em branco
        identificadores = myheart.readline().strip().split(',')

        for linhas in myheart:
            # faz o split de uma linha e guarda em linhas
            valores = linhas.strip().split(',')

            infos = {}
            for i in range(len(identificadores)):
                infos[identificadores[i]] = valores[i]

            dados.append(infos)

    return dados


def main():

    dados = get_dados_csv()

    saida = -1
    while saida != 0:
        print("1-Distribuição da doença por sexo")
        print("2-Distribuição da doença por escalões etários")
        print("3-Distribuição da doença por níveis de colesterol")
        print("4-Tabela da distribuição da doença por sexo")
        print("5-Tabela da distribuição da doença por escalões etários")
        print("6-Tabela da distribuição da doença por níveis de colesterol")
        print("0-Sair")

        saida = int(input("introduza a sua opcao-> "))
        if saida == 1:
            print(doenc_por_sexo(dados))
            print("----NEW----")
        elif saida == 2:
            print(doenc_nivel_colesterol(dados))
            print("----NEW----")
        elif saida == 3:
            print(doenc_nivel_colesterol(dados))
            print("----NEW----")
        elif saida == 4:
            print(tabela_doenc_por_sexo(dados))
            print("----NEW----")
        elif saida == 5:
            print(tabela_doenc_escalao_etario(dados))
            print("----NEW----")
        elif saida == 6:
            print(tabela_doenc_nivel_colesterol(dados))
            print("----NEW----")
        elif saida == 0:
            print("Saindo.....")
        else:
            print("Numero invalido")
            print("----NEW----")


if __name__ == "__main__":
    main()



