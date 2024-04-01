while True:
    print(f'\n \nEscolha uma opção: \n1. Validar E-mail \n2. Sair')
    escolha = input(f"\nDigite o número da opção desejada: ")
    if escolha == '1':
        email = input('Digite o endereço de e-mail para validação: ')
        if email.count('@') != 1:
            print(f'\nE-mail inválido')
            continue

        posicaoAt = email.find('@')
        posicaoPonto = email.rfind('.')

        if posicaoAt < 1 or posicaoAt > len(email) - 3 or posicaoPonto < posicaoAt + 2 or posicaoPonto == len(email) - 1:
            print(f'\nE-mail inválido')
        else:
            print(f'\nE-mail válido!')
    if escolha == '2':
        print('Saindo...')
        break