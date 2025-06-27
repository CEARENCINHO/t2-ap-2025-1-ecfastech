# Faça um programa que leia 5 números e informe a soma e a média dos números.

lista = []
somaLista = 0

while True:
    try:
        numero = int(input('Digite um numero: '))
    except ValueError:
        numero = int(input('APENAS NUEMEROS INTEIROS\nDigite um numero: '))
    
    lista.append(numero)
    opcao = input('Deseja continua? S ou N\n ')

    if opcao == 's' or opcao == 'S':
        continue
    elif opcao == 'n' or opcao == 'N':
        for i in lista:
            somaLista += i
        media = somaLista / len(lista) 
        print(f'A media é {media}')
        break
    