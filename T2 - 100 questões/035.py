# Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.
numero = int(input('Informe um numero: '))
lista_numero_primos = []
primo = []
qnd = 0
indice = numero

for numero in range(1,numero+1):
    primo = []
    qnd = 0
    for i in range(1,numero + 1):
        primo.append(numero%i)
    for i in range(len(primo)):
        if primo[i] == 0:
            qnd += 1
        else:
            continue
    if qnd == 2:
        lista_numero_primos.append(numero)
    else:
        continue
print(f'Numeros primos de 1 a {indice}')
print(*lista_numero_primos)