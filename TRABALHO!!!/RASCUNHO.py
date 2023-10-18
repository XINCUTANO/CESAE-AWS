# =
custo = 200
limpeza = 15
I = 200
D = 250
T = 275
S = 350
print("Selecione o tipo de quarto que reservou: (I-Individual, D-Duplo, T-Triplo ou S-Suite).")
tipodoquarto=input()
if(tipodoquarto==S):

    # solicitar ao utilizador numero do quarto
    print("Introduza o número do quarto de hotel S:")
    numquarto = int(input())

    # solicitar ao utilizador o numero de dias que esteve no quarto
    print("Quantos dias reservou este quarto? (Assuma um ano com 365 dias).")
    diasreservados = int(input())
    S=diasreservados*350
    print(S)

    #calcular valor iliquido
    valoriliquido=custo*diasreservados
    print("Valor iliquido:",valoriliquido)

    #calcular total do custo da limpeza
    totallimpeza=limpeza+15*diasreservados
    print("Custo da limpeza:",totallimpeza)

    #calcular valor de descontos fiscais a entregar ao estado
    descontosfiscais=valoriliquido*0.23
    print("O valor a entregar ao estado é:",descontosfiscais)

    #calcular o valor liquido a receber pelo quarto
    valorliquido=valoriliquido-totallimpeza-descontosfiscais
    print("O valor liquido a receber pelo quarto:",valorliquido)

