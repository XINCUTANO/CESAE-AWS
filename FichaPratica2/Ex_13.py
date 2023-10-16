# ler horas
horas = int(input("Horas: "))

# ler minutos
minutos = int(input("Minutos: "))

if(horas>12): # caso PM
    print(horas-12, ":", minutos, "PM")
else: # caso AM
    print(horas, ":", minutos, "AM")