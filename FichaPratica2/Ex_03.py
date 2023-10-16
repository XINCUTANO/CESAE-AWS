
# ler salario anual
salario=float(input("Insira o salário anual: "))

# condição para pagar 20% taxa
if(salario<=15000):
    imposto = salario * 0.2
    print("Paga taxa de 20 porcento:", imposto, "€")

# condição para pagar 30% taxa
if(salario>15000 and salario<=20000):
    imposto = salario * 0.3
    print("Paga taxa de 30 porcento:", imposto, "€")

# condição para pagar 35% taxa
if(salario>20000 and salario<=25000):
    imposto = salario * 0.35
    print("Paga taxa de 35 porcento:", imposto, "€")

# condição para pagar 40% taxa
if(salario>25000):
    imposto = salario * 0.4
    print("Paga taxa de 40 porcento:", imposto, "€")