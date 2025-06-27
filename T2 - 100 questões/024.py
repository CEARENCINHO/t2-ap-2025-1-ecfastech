# Faça um programa que calcule e mostre a média aritmética de N notas.

qunatidadeDeAlunos = int(input('Quantas notas irá digitar: '))
nota = 0
for i in range(qunatidadeDeAlunos):
    nota += float(input('Digite a nota do aluno:    '))
print(f'A média aritmetrica é {nota/qunatidadeDeAlunos}')