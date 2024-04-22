def cadastrar_suporte():
    """ Função responsável por cadastrar um novo suporte """
    print('Cadastrando Suporte')


opcao = input('Escolha uma opção Abaixo:\n'
              '1 - Cadastrar\n'
              '2 - Listar\n'
              '3 - Atualizar\n'
              '4 - Deletar\n'
              '5 - Sair\n')

match opcao:
    case '1':
        cadastrar_suporte()
