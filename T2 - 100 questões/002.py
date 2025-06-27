# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mstrando uma mensagem de erro e voltando a pedir as informações.

# pedi o usuario e a senha

usuario = ['adm']
senha = ['123adm']

entradaUsuario = input('Seu usuario:    ')
entradaSenha = input('Digite a sua senha:   ')
print('------------------------------')
if entradaUsuario in usuario:
    indiceUsuario = usuario.index(entradaUsuario)
    if entradaSenha == senha[indiceUsuario]:
        # adicionar mais usuarios
        print(f'Bem vindo {entradaUsuario}')
        while True:
            try:
                print('------------------------------')
                funcao = int(input('     Funções\n1 - Adicionar mais usuario\n2 - Remover usuarios\n3 - Mostrar listas de usuarios\n4 - Sair'))
            except ValueError:
                print('------------------------------')
                print('SOMENTE 1 2 E 3! NÃO DIGITE OUTRO ALEM DESSAS OPÇÕES!')
                funcao = int(input('     Funções\n1 - Adicionar mais usuario\n2 - Remover usuarios\n3 - Mostrar listas de usuarios\n4 - sair'))
            if funcao == 1:
                print('------------------------------')
                addUsuario = input('Digite o nome do novo usuario: ')
                addSenha = input(f'Digite a senha do usuario {addUsuario}: ')
                usuario.append(addUsuario)
                senha.append(addSenha)
                print(f'Usuario {addUsuario} criado com sucesso!')
                continue
            elif funcao == 2:
                print('------------------------------')
                print('Qual usuario deseja remover')
                for i in usuario:
                    i = usuario.index(i)
                    print(f'{i} - Usuario: {usuario[i]} Senha: {senha[i]}')
                try:
                    removeUsuario = int(input('Qual dos usuario quer remover? '))
                except ValueError:
                    print('Dgite apenas as opções acima: ')
                    removeIndice = int(input('Qual dos usuario quer remover? '))
                usuario.pop(removeIndice)
                senha.pop(removeIndice)
                print('Usuario removido!')
                for i in usuario:
                    i = usuario.index(i)
                    print(f'{i} - Usuario: {usuario[i]} Senha: {senha[i]}')
                continue
            elif funcao == 3:
                print('\nTodos os usuario e senha salvos')
                for i in usuario:
                    i = usuario.index(i)
                    print(f'{i} - Usuario: {usuario[i]} Senha: {senha[i]}')
                continue
            elif funcao == 4: 
                print('------------------------------')
                print('Você esta saindo!')
                break


                    
                

            
# quando tiver logado permitir adicionar mais usuarios