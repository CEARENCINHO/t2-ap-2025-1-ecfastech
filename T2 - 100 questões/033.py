# O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

hora = int(input('Quantas horas de leitura quer informar?  '))
temperatura = []
maior = 0
menor = 0
soma = 0
media = 0

for i in range(hora):
    temperatura.append(float(input(f'Quantos graus fez as {i+1}: ')))

# pega o primerio indice da lista

for i in range(len(temperatura) + 1):
    for l in range(i):
        if maior > temperatura[l]:
            continue
        else:
            maior = temperatura[l]
print(f'{maior}º é a maior temperatura')

menor = maior
for i in range(len(temperatura) + 1):
    menor = maior
    for l in range(i):
        if menor < temperatura[l]:
            continue
        else:
            menor = temperatura[l]
print(f'{menor}º é a menor temperatura')

for i in temperatura:
    soma += i
media = soma / len(temperatura)
print(f'A temperatura média é {int(media)}')




# verifique se o indice[x] é maior do que o proximo indice
    # se sim
        # maior = indice[x]
    # se não continue