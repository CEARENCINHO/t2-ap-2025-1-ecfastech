#   Faça um programa que leia e valide as seguintes informações:
#   a) Nome: maior que 3 caracteres;

while True:
    try:
        nome = str(input('Digite seu nome (nome com mais de 3 caracter):\n      '))
    except ValueError:
        print('Digite penas letras!')
        nome = input('Digite seu nome (nome com mais de 3 caracter):\n      ')

    tamanho = len(nome)

    if tamanho >= 3:
        break
    else:
        print('Digite um nome com mais de 3 letras!')

#   b) Idade: entre 0 e 150;
while True:
    try:
        idade = int(input('Digite a sua idade: '))
    except ValueError:
        print('Digite apenas numero')
        idade = int(input('Digite a sua idade: '))
    
    if idade >= 0 and idade <= 150:
        break
    else:
        print('Sua idade é invalida, idade tem que esta entre 0 e 150')

#   c) Salário: maior que zero;
while True:
    try:
        salario = float(input('Informe seu salario: '))
    except ValueError:
        print('Digite apenas numeros')
        salario = float(input('Informe seu salario: '))

    if salario > 0:
        break
    else: 
        print('Digite o salario sendo maior que R$ 0,00')
        continue

#   d) Sexo: 'f' ou 'm';

while True:
    sexo = input('Qual é seu sexo? F ou M: ')
    if sexo == 'f' or sexo == 'F':
        sexo = 'Feminino'
        break
    elif sexo == 'm' or sexo == 'M':
        sexo = 'Masculino'
        break
    else:
        print('Entrada invalida! Digite somente F ou M')
        continue

#   e) Estado Civil: 's', 'c', 'v', 'd';
while True:
    estadoCivil = str(input('Estado civil:\nS - Solteiro\nC - Casado\nV - Viuvo\nD - Divociado\n'))
    if estadoCivil == 's' or estadoCivil == 'S':
        estadoCivil = 'solteiro'
        break
    elif estadoCivil == 'c' or estadoCivil == 'C':
        estadoCivil = 'casado'
        break
    elif estadoCivil == 'v' or estadoCivil == 'V':
        estadoCivil = 'viuvo'
        break
    elif estadoCivil == 'd' or estadoCivil == 'D':
        estadoCivil = 'divociado'
        break
    else:
        print('Entrada invalida! Digite apenas as opções indicada abaixo:')
        continue

print(f'''
Seu nome é {nome}, e a sua idade é de {idade} anos e de sexo {sexo}.
Atualmente ganhar R$ {salario} e seu estado civil é {estadoCivil}
''')
#   Use a função len(string) para saber o tamanho de um texto (número de caracteres).