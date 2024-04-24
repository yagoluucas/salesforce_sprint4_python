def cadastrar_suporte():
    """ Função responsável por cadastrar um novo suporte """
    print('Cadastrando Suporte')


def listar_todos_os_suportes():
    """ Função responsável por listar todos os suportes do banco de dados """
    print('Todos os suportes')


def listar_suporte_pelo_id():
    """ Função responsável por listar suporte pelo id """
    id = 0
    while True:
        try:
            id = int(input('Digite o id do suporte: '))
            break
        except:
            print('O id deve ser um numero inteiro')
            continue
    print(f'Suporte com o id {id} recuperado')



def atualizar_suporte():
    """ Função responsável por atualizar um suporte """
    print('Suporte atualizado')


def deletar_suporte():
    """ Função responsável por deletar um suporte """
    print('Deletando suporte')


while True:
    opcao = input('Escolha uma opção Abaixo:\n'
                  '1 - Cadastrar\n'
                  '2 - Listar\n'
                  '3 - Listar suporte pelo id\n'
                  '4 - Atualizar\n'
                  '5 - Deletar\n'
                  '6 - Sair\n')
    match opcao:
        case '1':
            cadastrar_suporte()
        case '2':
            listar_todos_os_suportes()
        case '3':
            listar_suporte_pelo_id()
        case '4':
            atualizar_suporte()
        case '5':
            deletar_suporte()
        case '6':
            print('Encerrando o sistema...')
            break
        case _:
            print('Escolha uma opção válida')

