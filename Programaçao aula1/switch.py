#Casos em Python
estacao_ano=3
match estacao_ano:
    case 1:
        print("Primavera")
    case 2:
        print("Verão")
    case 3:
        print("Outono")
    case 4:
        print("Inverno")
    case _: #default
        print("Valor Inválido")
