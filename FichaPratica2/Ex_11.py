# ler saldo
saldo= float(input("Insira o saldo: "))

# ler valor a movimentar
movimento= float(input("Insira o valor a movimentar: "))

# verificar se a operacao é válida
saldoAposMovimento= saldo+movimento

if(saldoAposMovimento>=0): # operacao válida
    print("Operação realizada com sucesso")
    print("Saldo Atual:", saldoAposMovimento)
else:
    print("Operação Inválida! Saldo insuficiente")
    print("Saldo Atual:", saldo)
