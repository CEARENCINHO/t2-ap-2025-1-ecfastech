# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

from random import*
conjunto = []


soma = 0

for i in range(5):
    conjunto.append(randint(0,100))

maior = conjunto[0]
manor = conjunto[0]

for i in range(5):
    
    if maior > conjunto[i]:
        continue
    else:
        maior = conjunto[i]
    if manor < conjunto[i]:
        continue
    else:
        menor = conjunto[i]

for i in conjunto:
    soma += i    

print(f'conjunto {conjunto}\nManor numero do conjunto: {manor}\nMaior numero do conjunto: {maior}\nSoma dos conjuntos é: {soma}')

