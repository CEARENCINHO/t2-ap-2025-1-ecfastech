#   Faça um programa que leia 5 números e informe o maior número

from random import*

lista = []
maior = 0
for i in range(5):
    lista.append(randint(0,100))
print(lista)

for i in range(len(lista)):
    if maior > lista[i]:
        continue
    else:
        maior = lista[i]

print(maior)