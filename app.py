import os 

dados = [{'nome': 'admin', 'senha': '1234'}]

def login():
    os.system('cls')
    nome = input('Digte seu usuário ')
    encontrado = False
    for dado in dados:
        if nome == dado['nome']:
            encontrado = True
            senha = input('Digite sua senha ')
            if senha == dado['senha']:
                print('tudo certo')
            else:
                print('senha incorreta')
                input('digite algo para voltar ')
                main()
    if not encontrado:
        print('Usuário incorreto')
        input('digite algo para voltar ')
        main()

def cadastro():
    os.system('cls')
    nome = input('Digite o nome de usuario para cadastrar : ')
    encontrado = False
    for dado in dados:
        if dado['nome'] == nome:
            encontrado = True
            print('usuario ja cadastrado, tente outro.')
            input('Digite algo para voltar ')
            cadastro()
    if not encontrado:
        senha = input('Crie sua senha: ')
        dados.append({'nome':nome, 'senha':senha})
        print(f'Usuário: {nome} cadastrado com sucesso.')
        input('Digite algo para voltar ')
        main()

def escolha_usuario():
    print('SISTEMA DE REGISTRO E LOGIN \n')
    escolha = int(input('Digite 1 para login e 2 para cadastro: '))
    if escolha == 1:
        login()
    elif escolha ==2:
        cadastro()
    else:
        os.system('cls')
        print('Comando desconhecido!!! \n')
        input('Digite qualquer tecla ')
        main()

def main():
    os.system('cls')
    print(dados)
    escolha_usuario()

if __name__ == '__main__':
    main()