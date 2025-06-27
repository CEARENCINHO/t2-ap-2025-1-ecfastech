# Faça um programa que peça para n pessoas a sua idade, ao final o programa deverá verificar se a média de
# idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa,
# conforme a média calculada
somaTotal = 0
quantidadeAlunos = int(input('Quantos alunos tem: '))

for i in range(quantidadeAlunos):
    somaTotal += int(input(f'Informe a idade do aluno {i}:  '))

if int(somaTotal/quantidadeAlunos) < 25:
    print('A turma é jovem')
elif int(somaTotal/quantidadeAlunos) < 60:
    print('A turma é adulta')
else:
    print('A turma é idosa')