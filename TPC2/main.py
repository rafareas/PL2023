

def somado_on_of():

    soma = 0
    somaTmp = 0
    state = True
    caracteres = []
    stdin = input("Introduza uma sequencia:")

    while True:
        for c in stdin:
            caracteres.append(c)
        for i in range(len(caracteres)):
            if caracteres[i].isdigit() and state == True:
                soma += int(caracteres[i])
            elif caracteres[i].lower() == "o":
                if caracteres[i+1].lower() == "f" and caracteres[i+2].lower() == "f":
                    print("comportamento desativado")
                    state = False
                if caracteres[i+1].lower() == "n":
                    print("Comportamento ativado")
                    state = True
            elif caracteres[i] == "=":
                print(soma)
        caracteres = []
        stdin = input()
    return soma


def main():
    soma = somado_on_of()


if __name__ == "__main__":
    main()
