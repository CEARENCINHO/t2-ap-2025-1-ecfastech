# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
fibonacci = []

while True:
    if len(fibonacci) < 2:
        fibonacci.append(1)
    else:
        soma = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(soma)
    if fibonacci[-1] >= 500:
        print(fibonacci)
        break
    else:
        continue
print('aaaaa')