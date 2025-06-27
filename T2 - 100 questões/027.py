# Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos

alunos = []
media = 0
alunoTotal = 0

turma = int(input('Quantas turma tem? '))

for i in range(turma):
    alunos.append(int(input(f'Quantos aluno tem na turma {i}?')))
    alunoTotal += alunos[i]
    media = alunoTotal / len(alunos)

print(f'A média é de {media} por turma')