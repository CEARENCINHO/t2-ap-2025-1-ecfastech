# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao
# segundo número. Não utilize a função de potência da linguagem.

import math

base = int(input('Digite um numero: '))
ex = int(input('Digite um numero: '))

produto = math.pow(base,ex)

print(produto) 