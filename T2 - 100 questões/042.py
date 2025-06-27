conjunto_numerico = []
a1 = 0
a2 = 0
a3 = 0
a4 = 0
while True:
    numero = int(input('Digite um numero (digite numero negativo para sair): '))
    if numero > 0:
        conjunto_numerico.append(numero)
    else:
        break

for i in conjunto_numerico:
    if i <= 100 and i >= 76:
        a4 += 1
    elif i <= 75 and i >= 51:
        a3 += 1
    elif i <= 50 and i >= 26:
        a2 += 1
    elif i <= 25 and i >= 0:
        a1 += 1

print(f'[0-25] = {a1}\n[26-50] = {a2}\n[51-75] = {a3}\n[76-100] = {a4}')


