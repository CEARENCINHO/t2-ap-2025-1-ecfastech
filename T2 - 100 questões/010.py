# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

primeiroNumero = int(input('Escolha um numero: '))
segundoNumero = int(input('Escolha um outro numero: '))

lista = []

for i in range(primeiroNumero, segundoNumero):
    lista.append(i)

meioTermo = int(len(lista) / 2)
print(f' O meio termo dos numeros {primeiroNumero} e {segundoNumero} é o numero {lista[meioTermo]}')