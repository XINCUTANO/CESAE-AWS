
# ler nota 1
nota1=float(input("Insira a nota 1: "))

# ler nota 2
nota2=float(input("Insira a nota 2: "))

# ler nota 3
nota3=float(input("Insira a nota 3: "))

# calcular a media ponderada
mediaPonderada = (nota1*0.25) + (nota2*0.35) + (nota3*0.4)
print("Media Ponderada: ", mediaPonderada)

# avaliar se o aluno está ou não aprovado
if(mediaPonderada>=9.5):
    print("Aluno Aprovado")
else:
    print("Aluno Reprovado")
