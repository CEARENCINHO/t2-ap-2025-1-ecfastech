# banco de dados
banco_de_dados = [
    ['Joao',0],
    ['José',0],
    ['Alberto',0],
    ['Antonio',0],
    ['Branco',0],
    ['Nulo',0],
    ['FIM',0]
]

total = 0

maior_palavra = 0
for i in range(len(banco_de_dados)):
    if banco_de_dados[i][0] in ['Branco','Nulo','FIM']:
        continue
    else:
        if maior_palavra < len(banco_de_dados[i][0]):
            maior_palavra = len(banco_de_dados[i][0])


# input dos votos

while True:
    for i in range(len(banco_de_dados)):
        print(f'{i+1} - {banco_de_dados[i][0]}')
    voto = int(input('Digite seu voto: '))
    voto -= 1
    if voto == 6:
        print('FIM VOTAÇÃO')
        break
    elif voto > len(banco_de_dados) or voto < 0:
        print('Digite somente os numeros da tabela!')
    else:
        banco_de_dados[voto][1] += 1


# total para cada canditado
# total de nulo
# total de votos brancos

print('Resultados')
for i in range(len(banco_de_dados)-1):
    print(f'{banco_de_dados[i][0]} - {banco_de_dados[i][1]} votos')
    total += banco_de_dados[i][1]


print(f'NULOS% = {(banco_de_dados[5][1]/total):.2f}%')
print(f'BRANCOS% = {(banco_de_dados[4][1]/total):.2f}%')
# % de nulos sobre o total de votos

# % de votos brancos sobre o total de votos
  