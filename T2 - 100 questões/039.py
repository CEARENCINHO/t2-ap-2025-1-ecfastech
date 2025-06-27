#Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas., o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

dado = []

for i in range(5):
    aluno = int(input('Infomre o numero do aluno: '))
    altura = int(input(f'Infomre a altura do aluno {aluno}: '))
    dado.append([aluno,altura])

maior = dado[0][1]
for i in range(len(dado)-1):
    if maior > dado[i][1]:
        continue
    else:
        maior = dado[i][1]
        a = dado[i]

print(f'Codigo {a[0]} tem a maior altura de {maior}cm')
    


