# ler numero 1
a = int(input("Insira numero 1: "))

# ler numero 2
b = int(input("Insira numero 2: "))

# ler numero 3
c = int(input("Insira numero 3: "))

# a mais pequeno
if (a < b and a < c):
    if (b < c):
        print(a, b, c)
    else:
        print(a, c, b)

# b mais pequeno
if (b < a and b < c):
    if (a < c):
        print(b, a, c)
    else:
        print(b, c, a)

# c mais pequeno
if (c < a and c < b):
    if (a < b):
        print(c, a, b)
    else:
        print(c, b, a)