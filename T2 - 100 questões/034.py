# Os números primos possuem várias aplicações dentro da Computação, por exemplo na criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

numero = int(input('Informe um numero: '))
primo = []
qnd = 0

for i in range(1,numero + 1):
    primo.append(numero%i)
for i in range(len(primo)):
    if primo[i] == 0:
        qnd += 1
    else:
        continue
if qnd == 2:
    print(f'{numero} é numero primo')
else:
    print(f'{numero} não é numero primo!')