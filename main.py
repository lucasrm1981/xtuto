def calculadora():
    ## While e Switch +, - , / * e **
    n1 = float(input("Digite o primeiro numero"))
    n2 = float(input("Digite o segundo numero"))
    opcao = input("Deseja usar a calculadora? s ou n")

    while opcao != "n":
        calc = int(input("1 - soma\n 2 - sub\n 3 - mult\n4 - div\n5 - pot\n6 - Resto"))
        match calc:
            case 1:
                print(n1 + n2)
            case 2:
                print(n1 - n2)
            case 3:
                print(n1 * n2)
            case 4:
                print(n1 / n2)
            case 5:
                print(n1 ** n2)
            case 6:
                if n1 < n2:
                    print(n2 % n1)
                else:
                    print(n1 % n2)
        opcao = input("Deseja usar a calculadora? s ou n")


def boletim():
    ## Calculo de boletim a media tem que ser
    # A 9 ate 10, B 7 ate 9, C 5 ate 7 D < 5

    n1 = float(input("Digite a primeira nota"))
    n2 = float(input("Digite a segunda nota"))
    n3 = float(input("Digite a terceira nota"))
    n4 = float(input("Digite a quarta nota"))
    media = (n1 + n2 + n3 + n4) / 4
    if media >= 9 and media <= 10:
        print("Passou com Notão A")
    elif media >= 7 and media < 9:
        print("Passou com B")
    elif media >= 5 and media < 7:
        print("Passou com C")
    elif media >= 0 and media < 5:
        print("Reprovado")
    else:
        print("A nota tem que ser de 0 até 10")


def fatorial(num):
    ## Fatorial 3! = 3*2*1=6
    numero = int(input("Digite um numero para ser calculado"))
    ##Indice do while parada em 1
    indice = 1
    ## Fatorial Calculando em 1
    f = 1
    while indice <= numero:
        f = f * indice
        indice += 1
    ## Saida fora do while
    print("Fatorial While", numero, "! é", f)

    ### Saida com While

    ## Saida com for
    resultado = 1  ## Varivel que recebera o valor
    ## n será o inteiro
    for n in range(1, numero + 1):
        resultado *= n

    print("Fatorial FOR", resultado)


escolha = int(input("\n1-Calculadora\n2-Boletim\n3-Fatorial\n"))

match escolha:
    case 1:
        calculadora()
    case 2:
        boletim()
    case 3:
        fatorial()






