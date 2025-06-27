# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

di = 0
a = 0
numeros = []
num = int(input('Digite um numero: '))

for i in range(num):
    numeros.append(num % (i+1))
for i in numeros:
    if i == 0:
        a += 1
    else:
        continue
if a == 2:
    print('Primo')
else:
    print('Não primo')