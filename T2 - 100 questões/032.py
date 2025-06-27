# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário
fatorial = int(input('Fatorial de: '))
calculo = []
a = 1
resulte = fatorial

for i in range(fatorial * 2):
    if len(calculo) == 0:
        calculo.append(fatorial)
    elif (len(calculo) % 2) == 0:
        calculo.append(fatorial - a)
        a += 1
    elif (len(calculo) % 2) != 0:
        calculo.append(' . ')
calculo.pop(len(calculo)-1)
a = 0
for l in range(1,fatorial):
    a = resulte * l
    resulte = a

calculo_formatado = ''.join(map(str, calculo))
print(f'{fatorial}! = {calculo_formatado} = {resulte}')