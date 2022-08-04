import os

os.system('cls' or 'clear')

#Exercicio 5

palavra = input('Informe uma palavra: ')
palavraInvertida = ''


for i in range(len(palavra)-1, -1, -1):
    palavraInvertida = palavraInvertida + palavra[i]

print(palavraInvertida)

