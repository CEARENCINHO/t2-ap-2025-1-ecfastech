#Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
#    a) Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
#    b) Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
#    c) A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do
#       ano anterior. Faça um programa que determine o salário atual deste funcionário. Após concluir isto,
#       altere o programa permitindo que o usuário digite o salário inicial do funcionário.


def salario(si,eea):
    
    ano = 2025 - eea
    tempo = 2025 - ano

    if ano == 1:
        print(f'{ano} = R$ {si}')
    elif ano == 2:
        print(f'{ano} = R$ {si}')
        print(f'{ano + 1} = R$ {si * 1.015}')
    elif ano > 2:
        print(f'{ano} = R$ {si}')
        print(f'{ano + 1} = R$ {si * 1.015}')
        ano += 2
        salario2ano = si * 1.015
        porcentual = 0.015
        for i in range(tempo - 1):
            salario = salario2ano(1 + porcentual)
            print(f'{ano + i} = R$ {salario}')
            porcentual = porcentual * 2

    

salarioIncial = float(input('Informe o salario inicial: '))
empoEmpresaAno = int(input('Quanto tempo de empresa: '))

salario(salarioIncial,empoEmpresaAno)