saldoMedio = float(input("Saldo Médio 2023: "))

if (saldoMedio <= 2000):
    print("Nenhum crédito")
elif (saldoMedio > 2000 and saldoMedio <= 4000):
    print("Crédito Concedido:", (saldoMedio * 0.2))
elif (saldoMedio > 4000 and saldoMedio <= 6000):
    print("Crédito Concedido:", (saldoMedio * 0.3))
else:
    print("Crédito Concedido:", (saldoMedio * 0.4))