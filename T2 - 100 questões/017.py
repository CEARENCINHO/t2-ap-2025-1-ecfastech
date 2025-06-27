# A série de Fibonacci é formada pela sequência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série
# até que o valor seja maior que 500.

fator = int(input('Digite um numero: '))
fatorial = 1

for i in range(fator):
    i += 1
    fatorial = fatorial * i
print(f'O fatorial de {fator} é {fatorial}')