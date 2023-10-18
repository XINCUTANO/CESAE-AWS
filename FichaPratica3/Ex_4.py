
numero_misterioso = int(input("Número mistério: "))

tentativa1 = int(input("Tente adivinhar o número mistério: "))

if tentativa1 == numero_misterioso:
    print("Parabéns! Acertou.")
else:
    if tentativa1 < numero_misterioso:
        print("O número misterioso é maior.")
    else:
        print("O número misterioso é menor.")

    tentativa2 = int(input("Tente novamente: "))

    if tentativa2 == numero_misterioso:
        print("Parabéns! Acertou.")
    else:
        print("Errado. O número misterioso era", numero_misterioso)