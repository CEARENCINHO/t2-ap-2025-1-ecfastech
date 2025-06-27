#Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário

indice = int(input('Montar a tabuada de: '))
inicio = int(input('Começar por: '))
final = int(input('Terminar em: '))

while True:
    
    inicio = int(input('\nVocê digitou o inicio maior que o final, digite novamente!\nComeçar por: '))
    final = int(input('Terminar em: '))
    
    if inicio < final:
        break
    else:
        continue

print(f'\nVou montar a tabuada de {indice} começando em {inicio} e terminando em {final}:')
for i in range(inicio, final+1):
    print(f'{indice} X {i} = {indice*i}')