# O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:

valor = float(input('Preço do pão:'))

print('Panificadora Pão de ontem - Tabela de preços')
for i in range(50):
    print(f'{i+1} - R${(i+1) *valor}')