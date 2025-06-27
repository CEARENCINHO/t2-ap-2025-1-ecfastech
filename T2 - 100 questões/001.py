#   Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

# Bloco try para evitar erro caso o usuario digite um dado de valor String
try:
    nota = float(input('Digite uma nota de 0 a 10 (OBS: Não pode ser nada mais além de 0 a 10!):\n      '))
except ValueError:
    nota = float(input('Valor invalida: Digite numero: '))

# Laço de repetição para teste 
while True:

    if nota >= 0 and nota <= 10:
        print(f'\n  Sua nota é {nota}')
        break
    else:
        nota = float(input('\n    Valor invalido!\n   Digite somente de 0 a 10\nDigite sua nota: '))
        continue