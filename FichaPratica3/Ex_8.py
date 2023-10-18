
num=0
somatorio=0
contador=0

while(num!=-1):
    print("Introduza um numero:")
    if(num!=-1):
        num=int(input())
    somatorio=num+somatorio
    contador=contador+1
media=somatorio/contador
print("Media:",media)
