# ler duração música 1
musica1_minutos=int(input("Introduza os minutos da musica 1: "))
musica1_segundos=int(input("Introduza os segundos da musica 1: "))

# ler duração música 2
musica2_minutos=int(input("Introduza os minutos da musica 2: "))
musica2_segundos=int(input("Introduza os segundos da musica 2: "))

# ler duração música 3
musica3_minutos=int(input("Introduza os minutos da musica 3: "))
musica3_segundos=int(input("Introduza os segundos da musica 3: "))

# ler duração música 4
musica4_minutos=int(input("Introduza os minutos da musica 4: "))
musica4_segundos=int(input("Introduza os segundos da musica 4: "))

# ler duração música 5
musica5_minutos=int(input("Introduza os minutos da musica 5: "))
musica5_segundos=int(input("Introduza os segundos da musica 5: "))

# calcular o total do album em segundos
total_album_segundos=((musica1_minutos+musica2_minutos+musica3_minutos+musica4_minutos+musica5_minutos)*60)+(musica1_segundos+musica2_segundos+musica3_segundos+musica4_segundos+musica5_segundos)

# calcular as horas totais (multiplicar segundos totais por 3600)
horas=int(total_album_segundos/3600)

# calcular os minutos (tiro o tempo que já foi atribuido em horas)
minutos=int(total_album_segundos/60)-(horas*60)

# calcular os segundos (tiro a tempor que já foi atribuido em horas e em minutos)
segundos=total_album_segundos-(horas*3600)-(minutos*60)

# apresentar o resultado formatado
print(horas,":",minutos,":",segundos)

