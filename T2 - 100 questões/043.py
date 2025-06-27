cardapio = [
    ["Cachorro Quente", 100, 1.20],
    ["Bauru Simples", 101, 1.30],
    ["Bauru com ovo", 102, 1.50],
    ["Hambúrguer", 103, 1.20],
    ["Cheeseburguer", 104, 1.30],
    ["Refrigerante", 105, 1.00]
]
cabecalhos = ["Item", "Código", "Preço"]
pedido = []

codigo = 0
valor = 0
largura_item = 20
largura_codigo = 10
largura_preco = 10

print(f"{cabecalhos[0]:<{largura_item}} {cabecalhos[1]:<{largura_codigo}} {cabecalhos[2]:<{largura_preco}}")

for item in cardapio:
    nome_item = item[0]
    codigo_item = item[1]
    preco_item = item[2]

    preco_formatado = f"R$ {preco_item:.2f}"

    print(f"{nome_item:<{largura_item}} {codigo_item:<{largura_codigo}} {preco_formatado:<{largura_preco}}")

print('\nDigite 000 para encerrar pedido')
while True:
    codigo = int(input('Faça seu pedido apartir do codigo: '))
    
    if codigo <= 105 and codigo >= 100:
        if codigo == 0:
            break
        else:
            pedido.append(codigo_item)
            for i in range(len(cardapio)):
                if pedido[-1] == cardapio[i][1]:
                    valor += cardapio[i][2]
            print(f'R${valor:.2f}\n')
            continue
    elif codigo == 000:
        print(f'Valor total R${valor}')
        print('Pedido encerrado')
        break
    else:
        print('digite apenas os codigos da tabela')

