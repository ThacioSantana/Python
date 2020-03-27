#Manipulação de texto

# fateamento de frase
frase = 'curso em video python'

print(frase[9:21])
print(frase[:5])
print(frase[4:21:3])
print(frase[15:])
print(frase[9::3])

# Análise
print(len(frase))
print(frase.count('o'))
print(frase.count('o', 0, 13))
print(frase.find('deo'))
print(frase.find('Android'))
print("curso" in frase)

#Transformação
print(frase.replace('python','Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())