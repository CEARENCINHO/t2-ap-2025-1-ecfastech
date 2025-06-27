# A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a
# série até o n−ésimo termo.
num = int(input('Digite um numero'))
fibonacci = []
a = True

for i in range(num):
    if len(fibonacci) < 2:
        numero = 1
        fibonacci.append(numero)
    else:
        if len(fibonacci) <= 3:
            tamanho = len(fibonacci)
            tamanho -= 1
            b = tamanho - 1
            soma = fibonacci[tamanho] + fibonacci[b]
            fibonacci.append(soma)    
        else:
            tamanho = len(fibonacci)
            tamanho -= 1
            b = tamanho - 1
            soma = fibonacci[tamanho] + fibonacci[b]
            fibonacci.append(soma)
print(fibonacci)