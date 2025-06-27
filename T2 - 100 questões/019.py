# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

from random import*
conjunto = []


soma = 0

for i in range(5):
    conjunto.append(randint(0,1000))

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

