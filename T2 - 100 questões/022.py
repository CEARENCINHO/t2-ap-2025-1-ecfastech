# Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível

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
i = 0
if a == 2:
    print('Primo')
else:
    print('Não primo')
    for l in range(num):
        l += 1
        b = num % l
        if b == 0:
            print(f'{num} é divisivel por {l}')
        else:
            continue