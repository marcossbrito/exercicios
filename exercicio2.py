import os

os.system('cls' or 'clear')

#Exercicio 2

i = 1
lista = [0, 1]
simOuNao = False
nFibonaci = int(input('Informe um número: '))

while lista[i] <= nFibonaci:
    i = i + 1
    lista.append(lista[i-2] + lista[i-1])

for i in lista:
    if i == nFibonaci:
        simOuNao = True

if simOuNao:
    print('O número {} pertence a sequência Fibonacci'.format(nFibonaci))
else:
    print('O número {} não pertence a sequência Fibonacci'.format(nFibonaci))