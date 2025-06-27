# Uma academia deseja fazer um censo entre seus clientes para descobrir o mais alto, o mais baixo, o mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do cliente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes

texto = ['seu codigo: ', 'sua altura: ', 'seu peso: ']
usuario = []
cadatros = []
alto = []
baixo = []


while True:
    usuario = []
    for i in range(3):
        dado = int(input(f'Informe {texto[i]}'))
        if dado == 0:
            break
        else:
            usuario.append(dado)
    cadatros.append(usuario)
    if dado == 0:
        break
    else:
        continue

maior = cadatros[0][1]
for i in range(len(cadatros)-1):
    if maior > cadatros[i][1]:
        continue
    else:
        maior = cadatros[i][1]
        a = cadatros[i]

print(f'Codigo {a[0]} tem a maior altura de {maior}cm')

maior = cadatros[0][2]
for i in range(len(cadatros)-1):
    if maior > cadatros[i][2]:
        continue
    else:
        maior = cadatros[i][2]
        a = cadatros[i]

print(f'Codigo {a[0]} tem o maior peso de {maior}cm')