
# ler o valor
montante = int(input("Insira o valor €: "))

if(montante%5==0): # é múltiplo de 5

    numeroNotas= int(montante/200)
    montante= montante%200
    print("\nNotas de 200:", numeroNotas)

    numeroNotas =int(montante/100)
    montante = montante % 100
    print("Notas de 100:", numeroNotas)

    numeroNotas = int(montante / 50)
    montante = montante % 50
    print("Notas de 50:", numeroNotas)

    numeroNotas = int(montante / 20)
    montante = montante % 20
    print("Notas de 20:", numeroNotas)

    numeroNotas = int(montante / 10)
    montante = montante % 10
    print("Notas de 10:", numeroNotas)

    numeroNotas = int(montante / 5)
    print("Notas de 5:", numeroNotas)

else: # valor inválido
    print("Valor Inválido. Deve ser múltiplo de 5!")