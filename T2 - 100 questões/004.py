#   Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de
#   crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
#   Faça um programa que calcule e escreva o número de anos necessários para que a população do país A
#   ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

populaçãoPais_A = 80000
populaçãoPais_B = 200000

taxaAnualPais_A = 0.03
taxaAnualPais_B = 0.015

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
        