# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a
# quantidade de números ímpares.

impar = 0
par = 0

for i in range(10):
    num = 0
    num = int(input('Digite um numero: '))
    num = num % 2
    if num == 0:
        par += 1
    elif num == 1:
        impar += 1

print(f'Entre esse 10 numeros tem:\n qnt de par:{par}\n qnt de impar:{impar}')