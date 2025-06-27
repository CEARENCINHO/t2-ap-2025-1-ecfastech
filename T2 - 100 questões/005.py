#   Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
#   Valide a entrada e permita repetir a operação
try:
    populaçãoPais_A = int(input('Quantos habitantes tem no país A:  '))
    populaçãoPais_B = int(input('Quantos habitantes tem no país B:  '))
except ValueError:
    print('Apenas valor numerico e valor numerico sem decimal:')
    populaçãoPais_A = int(input('Quantos habitantes tem no país A:  '))
    populaçãoPais_B = int(input('Quantos habitantes tem no país B:  '))

try:
    taxaAnualPais_A = float(input('Qual é o pencentual de crescimento do país A:   '))
    taxaAnualPais_B = float(input('Qual é o pencentual de crescimento do país B:   '))
except ValueError:
    print('Apenas valor numerico e valor numerico sem decimal:')
    taxaAnualPais_A = float(input('Qual é o pencentual de crescimento do país A:   '))
    taxaAnualPais_B = float(input('Qual é o pencentual de crescimento do país B:   '))

taxaAnualPais_A = taxaAnualPais_A / 100
taxaAnualPais_B = taxaAnualPais_B / 100

anos = 0
while True:
    populaçãoPais_A = int((populaçãoPais_A * taxaAnualPais_A) + populaçãoPais_A)
    populaçãoPais_B = int((populaçãoPais_B * taxaAnualPais_B) + populaçãoPais_B)

    if populaçãoPais_A >= populaçãoPais_B:
        print(f'O país A vai ultrapassar o país B após {anos} anos!')
        print(f'País A: {populaçãoPais_A}\nPaís B: {populaçãoPais_B}')
        break
    else:
        anos += 1
        continue
