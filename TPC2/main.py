

def somado_on_of():

    on = "on"
    off = "off"
    soma = 0
    while True:
        stdin = input("Introduza um número:")
        if stdin.lower() == off.lower():
            break
        elif stdin.lower() == on.lower():
            print('Comportamento reativado')
            True
        elif stdin == "=":
            print(soma)
        else:
            soma += int(stdin)

    return soma


def main():

    soma = somado_on_of()
    print(soma)



if __name__ == "__main__":
    main()
