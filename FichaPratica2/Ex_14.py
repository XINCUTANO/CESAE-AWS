# ler numero1
print("Introduza um numero:")
num1 = int(input())
# ler numero2
print("Introduza um numero:")
num2 = int(input())
# ler numero3
print("Introduza um numero:")
num3 = int(input())
if (num1 < num2) and (num1 < num3) and (num2 < num3):
    print(num1, num2, num3)
if (num1 < num3) and (num1 < num2) and (num3 < num2):
    print(num1, num3, num2)

if (num2 < num1) and (num2 < num3) and (num1 < num3):
    print(num2, num1, num3)

if (num2 < num3) and (num2 < num1) and (num1> num3):
    print(num2, num3, num1)

if (num3 < num1) and (num3 < num2) and (num2 < num1):
    print(num3, num2, num1)

if (num3 < num2) and (num3 < num1) and (num2 > num1):
    print(num3, num1, num2)
