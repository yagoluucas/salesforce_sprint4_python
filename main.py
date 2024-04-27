import json
import datetime

suporte = {'id_suporte': 1, 'nome_empresa': 'Fiap',
           'nome_pessoa': 'Yago', 'sobrenome_pessoa': 'Lucas',
           'descricao': 'Comprei um serviço e tenho duvidas de como usar', 'id_pais': 1}


def cadastrar_suporte():
    """ Função responsável por cadastrar um novo suporte """
    id_pais = 0
    while True:
        try:
            id_pais = int(input('Digite o id do pais: '))
        except:
            print('O id precisa ser um numero inteiro')
            continue
        nome_empresa = input('Digite o nome da sua empresa: ')
        nome_pessoa = input('Digite o seu nome: ')
        sobrenome_pessoa = input('Digite o seu sobrenome: ')
        descricao_suporte = input('Digite o motivo do contato: ')
        novo_suporte = {'nome_empresa': nome_empresa,
                        'nome_pessoa': nome_pessoa, 'sobrenome_pessoa': sobrenome_pessoa,
                        'descricao': descricao_suporte, 'id_pais': id_pais}
        atividade_do_site(1)
        break

    print('Cadastrando Suporte')


def listar_todos_os_suportes():
    """ Função responsável por listar todos os suportes do banco de dados """
    lista_suporte = []
    match input('Deseja salvar essa consulta ? digite apenas numeros\n'
                '1 - Sim\n'
                '2 - Não\n'):
        case '1':
            salvar_json(lista_suporte)
        case '2':
            print('Retornando ao menu principal')
        case _:
            print('Opção incorreta')

    print('Todos os suportes')


def listar_suporte_pelo_id():
    """ Função responsável por listar suporte pelo id """
    while True:
        try:
            idSuporte = int(input('Digite o id do suporte ou 0 (zero) para sair: '))
            if idSuporte == 0:
                print('Retornando ao menu principal')
                break
        except:
            print('O id deve ser um numero inteiro')
            continue
        print(f'Suporte com o id {idSuporte} recuperado')
        match input('Deseja salvar essa consulta ? digite apenas numeros\n'
                    '1 - Sim\n'
                    '2 - Não\n'
                    ''):
            case '1':
                salvar_json([suporte])
                print('Suporte salvo, retornando ao menu')
            case '2':
                print('Retornando ao menu principal')
                break
            case _:
                print('Opção incorreta')



def atividade_do_site(idSuporte: int):
    """Função responsável por salvar uma atividade do site toda vez que um suporte é cadastrado"""
    array_data = datetime.datetime.now()
    ano = array_data.strftime('%y')
    mes = array_data.month
    dia = array_data.day
    print(ano, mes, dia)
    atividade_site = {'oportunidade': 'N', 'data': f'{ano}/{mes}/{dia}',
                      'id_suporte': idSuporte, 'id_teste_gratis': None}
    print(atividade_site)


def atualizar_suporte():
    """ Função responsável por atualizar um suporte """
    print('Suporte atualizado')


def deletar_suporte():
    """ Função responsável por deletar um suporte """
    print('Deletando suporte')


def salvar_json(lista_suporte: list):
    """ Função responsável por salvar a lista de suporte em um arquivo JSON """
    with open('arquivo/export_consulta.json', 'w', encoding='utf-8') as arquivo:
        json.dump(lista_suporte, arquivo, indent=4, ensure_ascii=False)


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
