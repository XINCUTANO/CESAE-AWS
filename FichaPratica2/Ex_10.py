
# ler num1
num1= float(input("Insira um número: "))

# ler num2
num2= float(input("Insira um número: "))

# ler operacao aritmetica
operacao= input("Operação (+ - * /): ")

# soma
if(operacao=="+"):
    resultado = num1 + num2
    print("Soma:",  resultado)

# subtracao
elif(operacao=="-"):
    resultado = num1 - num2
    print("Subtração:", resultado)

# multiplicacao
elif(operacao=="*"):
    resultado = num1 * num2
    print("Multiplicação:", resultado)

# divisao
elif(operacao=="/"):
    resultado = num1 / num2
    print("Divisão:", resultado)

else:
    print("Erro! Operação Inválida!")