import json
import datetime
import pwinput
import oracledb

suporte = {'id_suporte': 1, 'nome_empresa': 'Fiap',
           'nome_pessoa': 'Yago', 'sobrenome_pessoa': 'Lucas',
           'descricao': 'Comprei um serviço e tenho duvidas de como usar', 'id_pais': 1}

usuario = input('Digite o seu usuário: ')
senha = pwinput.pwinput('Digite a sua senha: ')

# Conexão com o banco de dados
try:
    conn = oracledb.connect(user=usuario,
                            password=senha,
                            host='oracle.fiap.com.br', 
                            service_name='ORCL')
    cursor = conn.cursor()
except Exception as error:
    conexao = False
    print(f'Erro ao se conectar: {error}') 
else:
    print('Conexão bem sucedida')
    conexao = True

def criar_suporte() -> dict:
    """ Função responsável por criar o suporte no banco de dados """
    novo_suporte = {}
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
        break
    return novo_suporte


def cadastrar_suporte():
    """ Função responsável por cadastrar um novo suporte """
    suporte = criar_suporte()
    query = """INSERT INTO TESTE_GRATIS"""
    print('Cadastrando Suporte')


def listar_suporte(filtro='all', parametro=''):
    """ Função responsável por listar todos os suportes do banco de dados """
    lista_suporte = []
    try:
        if filtro == 'all':
            query = """SELECT * FROM SUPORTE"""
        elif filtro == 'id_suporte':  
            query = f"""SELECT * FROM SUPORTE WHERE ID_SUPORTE = {parametro}"""
        else:
            query = f"""SELECT * FROM SUPORTE WHERE ID_PAIS = {parametro}"""
        cursor.execute(query)
        lista_suporte = cursor.fetchall()
        if len(lista_suporte) == 0:
            print('Nenhum suporte cadastrado')
            return
        else:
            while True:
                match input('Deseja salvar essa consulta ? digite apenas numeros\n'
                '1 - Sim\n'
                '2 - Não\n'):
                    case '1':
                        nome_arquivo = input('Digite o nome do arquivo: ')
                        salvar_json(lista_suporte, nome_arquivo)
                        print('Retornaodo ao menu principal')
                        return
                    case '2':
                        print('Retornando ao menu principal')
                        return
                    case _:
                        print('Opção incorreta')
    except Exception as error:
        print('Erro ao se conectar no banco de dados')    
    

    """ Esta função lista todos os suportes por data """
    data = input('Digite a data que você deseja buscar: ')


def atividade_do_site(id_suporte: int):
    """Função responsável por salvar uma atividade do site toda vez que um suporte é cadastrado"""
    array_data = datetime.datetime.now()
    ano = array_data.strftime('%y')
    mes = array_data.month
    dia = array_data.day
    print(ano, mes, dia)
    atividade_site = {'oportunidade': 'N', 'data': f'{ano}/{mes}/{dia}',
                      'id_suporte': id_suporte, 'id_teste_gratis': None}
    print(atividade_site)


def atualizar_suporte():
    """ Função responsável por atualizar um suporte """
    novo_suporte = criar_suporte()
    print('Suporte atualizado')


def deletar_suporte():
    """ Função responsável por deletar um suporte """
    print('Deletando suporte')


def salvar_json(lista_suporte: list, nome_arquivo: str):
    """ Função responsável por salvar a lista de suporte em um arquivo JSON """
    with open(f'arquivo/{nome_arquivo}.json', 'w', encoding='utf-8') as arquivo:
        nova_lista = []
        for item in lista_suporte:
            dicionario = {
                'id_suporte': item[0], 'nome_empresa': item[1],
                'nome_pessoa': item[2], 'sobrenome_pessoa': item[3],
                'descricao': item[4], 'id_pais': item[5]
            }
            nova_lista.append(dicionario)
        json.dump(nova_lista, arquivo, indent=4, ensure_ascii=False)
        print(f'Sucesso ao salvar as informações no arquivo :{nome_arquivo}')

while True:
    opcao = input('Escolha uma opção Abaixo:\n'
                  '1 - Cadastrar\n'
                  '2 - Listar\n'
                  '3 - Listar suporte pelo id\n'
                  '4 - Listar suporte pelo País\n'
                  '5 - Atualizar\n'
                  '6 - Deletar\n'
                  '7 - Sair\n')
    match opcao:
        case '1':
            cadastrar_suporte()
        case '2':
            listar_suporte()
        case '3':
            id_suporte = input('Digite o id do suporte: ')
            listar_suporte('id_suporte', id_suporte)
        case '4':
            id_pais = input('Digite o id do pais: ')
            listar_suporte('id_pais', id_pais)
        case '5':
            atualizar_suporte()
        case '6':
            deletar_suporte()
        case '7':
            print('Encerrando o sistema...')
            break
        case _:
            print('Escolha uma opção válida')
