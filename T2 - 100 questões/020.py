# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

while True:
    try:
        fator = int(input('Digite um numero: '))
    except ValueError:
        
        fator = int(input('Apenas inteiros\nDigite um numero: '))
    fatorial = 1
    if fator >= 16 and type(fator) == int:
        for i in range(fator):
            i += 1
            fatorial = fatorial * i
        print(f'O fatorial de {fator} é {fatorial}')
        opcao = input('Deseja continua: (S ou N)')
        if opcao != 'S' or opcao != 's':
            continue
        else:
            break
    else:
        print('Digite um valor inteiro e acima de 16!')
        continue
    