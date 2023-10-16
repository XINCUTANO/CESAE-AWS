# imprimir opcoes
print("1. Criar")
print("2. Atualizar")
print("3. Eliminar")
print("4. Sair")

# ler opcao
opcao= int(input("Opção: "))


if(opcao==1): # opcao 1
    print("\n***** Criar *****")

elif(opcao==2): # opcao 2
    print("\n***** Atualizar *****")

elif(opcao==3): # opcao 3
    print("\n***** Eliminar *****")

elif(opcao==4): # opcao 4
    print("")
else: # operacao inválida
    print("\nOperação Inválida")