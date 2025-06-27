# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para cada um.

valorCD = 0
media = 0

quantidadeCD = int(input('Quantos coleções tem? '))

for i in range(quantidadeCD):
    valorCD += float(input(f'Quantos foi o CD numero {i+1}: '))
    media = valorCD/(i+1)

print(f'Foi {quantidadeCD} coleções em media de R${media}')   