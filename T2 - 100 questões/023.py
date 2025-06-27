# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

di = 0
a = 0
numeros = []
num = int(input('Digite um numero: '))

for w in range(num+1):
    numeros = []
    a = 0
    for i in range(w):
        numeros.append(w % (i+1))
    for i in numeros:
        if i == 0:
            a += 1
        else:
            continue
    if a == 2:
        print(f'{w} é Primo')
    else:
        print(f'{w} não primo')