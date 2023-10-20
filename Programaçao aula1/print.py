a=3
a="FCP"
#MECANISMO DE TRATAMENTO DE ERROS
try:
    print("Indique a sua idade:")
    idade=int(input())
except:
    print("Deverá introduzir um numero inteiro.")
else:
    #nova forma de apresentar um print
    print(f"Idade: {idade}")
#eval=input()) funciona para todos os numeros int ou float
