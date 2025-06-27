dados_acidentes_1999 = [
    ["C001", "São Paulo", 23450, 3200000, 16800],
    ["C002", "Rio de Janeiro", 19320, 2150000, 14500],
    ["C003", "Belo Horizonte", 8764, 1090000, 6700],
    ["C004", "Salvador", 6543, 870000, 4800],
    ["C005", "Fortaleza", 5765, 790000, 4300],
    ["C006", "Curitiba", 7124, 950000, 5100],
    ["C007", "Porto Alegre", 6902, 880000, 4950],
    ["C008", "Recife", 5234, 810000, 3800],
    ["C009", "Goiânia", 4876, 700000, 3500],
    ["C010", "Manaus", 3542, 610000, 2600],
    ["C011", "Belém", 3104, 590000, 2400],
    ["C012", "Campinas", 2543, 520000, 1900],
    ["C013", "São Luís", 2110, 430000, 1600],
    ["C014", "Maceió", 1890, 400000, 1450],
    ["C015", "Natal", 1765, 390000, 1350],
    ["C016", "Campo Grande", 1654, 380000, 1250],
    ["C017", "Teresina", 1543, 370000, 1200],
    ["C018", "João Pessoa", 1434, 350000, 1100],
    ["C019", "São Bernardo do Campo", 1321, 340000, 1000],
    ["C020", "Santo André", 1234, 330000, 950],
    ["C021", "Osasco", 1123, 310000, 880],
    ["C022", "São José dos Campos", 1045, 300000, 820],
    ["C023", "Ribeirão Preto", 980, 290000, 760],
    ["C024", "Uberlândia", 934, 280000, 730],
    ["C025", "Sorocaba", 890, 270000, 700],
    ["C026", "Niterói", 854, 260000, 680],
    ["C027", "Londrina", 823, 250000, 660],
    ["C028", "Aracaju", 765, 240000, 610],
    ["C029", "Joinville", 734, 230000, 590],
    ["C030", "Juiz de Fora", 702, 220000, 570],
    ["C031", "Boa Esperança", 45, 1800, 38],
    ["C032", "Nova Aurora", 28, 1600, 22],
    ["C033", "Santa Rita do Pardo", 17, 1300, 15],
    ["C034", "Cedro do Abaeté", 10, 1100, 9],
    ["C035", "Lagoa dos Patos", 6, 950, 5],
    ["C036", "Serra da Saudade", 5, 900, 4],
    ["C037", "Borá", 3, 850, 3],
    ["C038", "Anhanguera", 4, 1200, 3],
    ["C039", "Araguainha", 2, 700, 2],
    ["C040", "Olho d'Água do Casado", 7, 1400, 6],
    ["C041", "Nova Castilho", 9, 1600, 7],
    ["C042", "Cedralzinho", 6, 1150, 5],
    ["C043", "Santo Antônio do Aventureiro", 12, 1700, 10],
    ["C044", "Pedro Teixeira", 10, 1900, 9],
    ["C045", "Chapada de Areia", 8, 1500, 6],
]

def lista():
    maior_palavra = 0
    quant_string = 0
    for i in range(len(dados_acidentes_1999)):
        if maior_palavra < len(dados_acidentes_1999[i][1]):
            maior_palavra = len(dados_acidentes_1999[i][1])
            print(dados_acidentes_1999[i][1])

    print('CODIGO  | CIDADE                        | ACIDENTES')
    for i in range(len(dados_acidentes_1999)):
        quant_string = maior_palavra - len(dados_acidentes_1999[i][1])
        print(f' {dados_acidentes_1999[i][0]}   | {dados_acidentes_1999[i][1]}',' '*quant_string,'| ', dados_acidentes_1999[i][4])
        

def media_carros_2000():
    indice = 0
    soma = 0
    for i in range(len(dados_acidentes_1999)):
        if dados_acidentes_1999[i][3] < 2000:
            soma += dados_acidentes_1999[i][4]
            indice += 1
        else:
            continue
    return soma / indice



def media_carros():
    soma = 0
    for i in range(len(dados_acidentes_1999)):
        soma += dados_acidentes_1999[i][3]
    return soma / len(dados_acidentes_1999)



def indice_acidente():
    maior = 0 
    for i in range(len(dados_acidentes_1999)):
        indice = dados_acidentes_1999[i][2] / dados_acidentes_1999[i][3]
        if maior < indice:
            maior = indice
            cidade = dados_acidentes_1999[i][1]
        else:
            continue
    print(f'Maior indice é da cidade de {cidade} com indice de {maior:.4f}')

    menor = maior
    for l in range(len(dados_acidentes_1999)):
        indice = dados_acidentes_1999[l][2] / dados_acidentes_1999[l][3]
        if menor > indice:
            menor = indice
            cidade = dados_acidentes_1999[l][1]
        else:
            continue
    print(f'Menor indice é da cidade de {cidade} com indice de {menor:.4f}')

print(lista())
print(indice_acidente())
print(f'Media de carros das cidades {media_carros():.2f}')
print(f'A media de carros das cidades ontem há menos de 2000 carros é de {media_carros_2000()}')