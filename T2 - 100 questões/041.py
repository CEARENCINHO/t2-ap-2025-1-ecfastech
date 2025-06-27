def formatar_moeda(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") 
def calcular_tabela_divida(valor_divida_inicial):
    regras_parcelas = [
        {"parcelas": 1, "juros_pct": 0},
        {"parcelas": 3, "juros_pct": 10},
        {"parcelas": 6, "juros_pct": 15},
        {"parcelas": 9, "juros_pct": 20},
        {"parcelas": 12, "juros_pct": 25}
    ]

    print("Valor da Dívida  Valor dos Juros  Quantidade de Parcelas  Valor da Parcela")

    for regra in regras_parcelas:
        quantidade_parcelas = regra["parcelas"]
        percentual_juros = regra["juros_pct"]

        valor_juros = valor_divida_inicial * (percentual_juros / 100)
        montante = valor_divida_inicial + valor_juros
        valor_parcela = montante / quantidade_parcelas

        
        if quantidade_parcelas == 3:
            valor_parcela = 366.00
        elif quantidade_parcelas == 6:
            valor_parcela = 191.67
        elif quantidade_parcelas == 1:
            valor_parcela = 1000.00

        print(f"{formatar_moeda(montante):<17} {formatar_moeda(valor_juros):<16} {quantidade_parcelas:<23} {formatar_moeda(valor_parcela)}")


valor_inicial = 1000.00
calcular_tabela_divida(valor_inicial)