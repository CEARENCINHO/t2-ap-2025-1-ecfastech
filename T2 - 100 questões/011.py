# Altere o programa anterior para mostrar no final a soma dos números.

primeiroNumero = int(input('Escolha um numero: '))
segundoNumero = int(input('Escolha um outro numero: '))

lista = []
soma = 0

for i in range(primeiroNumero, segundoNumero):
    lista.append(i)
    soma += i

meioTermo = int(len(lista) / 2)
print(f'O meio termo dos numeros {primeiroNumero} e {segundoNumero} é o numero {lista[meioTermo]}.\nA soma dos numeros é {soma}')