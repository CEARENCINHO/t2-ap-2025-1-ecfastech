# registrar e amarzena os preços dos produtos

valor_total_produtos = 0
contagem = 1 
dinheiro = 0


print('Loja Tabajara')
while True:
    valor = int(input(f'Produtos {contagem}: R$' ))
    contagem += 1
    if valor == 0:
        break
    else:
        valor_total_produtos += valor
        continue

print(f'Total R${valor_total_produtos}')
dinheiro = float(input('Dinheiro: R$'))
print(f'Troco R${valor_total_produtos - dinheiro}')
# quando o valor 0 for inputado deve retornar o valor da compra 
# retorna o valor total da compra e pergunta ao cliente o quando de dinheiro ele irá pagar para depois retornar o troco
# apos isso o programa deve retorna ao inicio para registrar uma nova compra

