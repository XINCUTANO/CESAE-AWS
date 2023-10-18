#=
custo=200
limpeza=15
I=200
D=250
T=275
S=350

#calcular lucro anual de um quarto


#solicitar ao utilizador o tipo de quarto
print("Selecione o tipo de quarto que reservou: (I-Individual, D-Duplo, T-Triplo ou S-Suite).")
tipodoquarto=input()

#calcular preço do quarto individual
if(tipodoquarto=="I"):
    # solicitar ao utilizador numero do quarto
    print("Introduza o número do quarto de hotel I:")
    numquarto = int(input())

    # solicitar ao utilizador o numero de dias que esteve no quarto
    print("Quantos dias reservou este quarto? (Assuma um ano com 365 dias).")
    diasreservados = int(input())

    valoriliquido = I * diasreservados
    print("Valor iliquido:", valoriliquido)

    # calcular total do custo da limpeza
    totallimpeza = limpeza * diasreservados
    print("Custo da limpeza:", totallimpeza)

    # calcular valor de descontos fiscais a entregar ao estado
    if (valoriliquido <= 20000):
        descontosfiscais = 0.23
    elif (valoriliquido > 20000) and (valoriliquido <= 50000):
        descontosfiscais = 0.25
    elif (valoriliquido > 50000):
        descontosfiscais = 0.28

    descontosfiscais=valoriliquido*descontosfiscais
    print("O valor a entregar ao estado é:", descontosfiscais)

    # calcular o valor liquido a receber pelo quarto
    valorliquido = valoriliquido - totallimpeza - descontosfiscais
    print("O valor liquido a receber pelo quarto:", valorliquido)

#calcular preço do quarto duplo
elif(tipodoquarto=="D"):
    # solicitar ao utilizador numero do quarto
    print("Introduza o número do quarto de hotel D:")
    numquarto = int(input())

    # solicitar ao utilizador o numero de dias que esteve no quarto
    print("Quantos dias reservou este quarto? (Assuma um ano com 365 dias).")
    diasreservados = int(input())

    print(D)
    valoriliquido = D * diasreservados
    print("Valor iliquido:", valoriliquido)

    # calcular total do custo da limpeza
    totallimpeza = (limpeza+5) * diasreservados
    print("Custo da limpeza:", totallimpeza)

    # calcular valor de descontos fiscais a entregar ao estado

    if (valoriliquido <= 20000):
        descontosfiscais = 0.23
    elif (valoriliquido > 20000) and (valoriliquido <= 50000):
        descontosfiscais = 0.25
    elif (valoriliquido > 50000):
        descontosfiscais = 0.28

    descontosfiscais=valoriliquido*descontosfiscais
    print("O valor a entregar ao estado é:", descontosfiscais)

    # calcular o valor liquido a receber pelo quarto
    valorliquido = valoriliquido - totallimpeza - descontosfiscais
    print("O valor liquido a receber pelo quarto:", valorliquido)

#calcular preço do quarto triplo
elif(tipodoquarto=="T"):
    # solicitar ao utilizador numero do quarto
    print("Introduza o número do quarto de hotel T:")
    numquarto = int(input())

    # solicitar ao utilizador o numero de dias que esteve no quarto
    print("Quantos dias reservou este quarto? (Assuma um ano com 365 dias).")
    diasreservados = int(input())
    I=diasreservados*275
    print(T)

    valoriliquido = T * diasreservados
    print("Valor iliquido:", valoriliquido)

    # calcular total do custo da limpeza
    totallimpeza = (limpeza + 5) * diasreservados
    print("Custo da limpeza:", totallimpeza)

    # calcular valor de descontos fiscais a entregar ao estado
    if (valoriliquido <= 20000):
        descontosfiscais = 0.23
    elif (valoriliquido > 20000) and (valoriliquido <= 50000):
        descontosfiscais = 0.25
    elif (valoriliquido > 50000):
        descontosfiscais = 0.28

    descontosfiscais=valoriliquido*descontosfiscais
    print("O valor a entregar ao estado é:", descontosfiscais)

    # calcular o valor liquido a receber pelo quarto
    valorliquido = valoriliquido - totallimpeza - descontosfiscais
    print("O valor liquido a receber pelo quarto:", valorliquido)

#calcular preço da suite
elif(tipodoquarto=="S"):
    # solicitar ao utilizador numero do quarto
    print("Introduza o número do quarto de hotel S:")
    numquarto = int(input())

    # solicitar ao utilizador o numero de dias que esteve no quarto
    print("Quantos dias reservou este quarto? (Assuma um ano com 365 dias).")
    diasreservados = int(input())
    print(S)

    #calcular valor iliquido
    valoriliquido=S*diasreservados
    print("Valor iliquido:",valoriliquido)

    #calcular total do custo da limpeza
    totallimpeza=(limpeza+15)*diasreservados
    print("Custo da limpeza:",totallimpeza)

    #calcular valor de descontos fiscais a entregar ao estado

    if (valoriliquido <= 20000):
        descontosfiscais = 0.23
    elif (valoriliquido > 20000) and (valoriliquido <= 50000):
        descontosfiscais = 0.25
    elif (valoriliquido > 50000):
        descontosfiscais = 0.28

    descontosfiscais=valoriliquido*descontosfiscais
    print("O valor a entregar ao estado é:",descontosfiscais)

    #calcular o valor liquido a receber pelo quarto
    valorliquido=valoriliquido-totallimpeza-descontosfiscais
    print("O valor liquido a receber pelo quarto:",valorliquido)
else:
    print("Esta tipologia está incorreta.")


