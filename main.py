import json
import pwinput
import oracledb


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
            cursor.execute(f'SELECT * FROM PAIS WHERE ID_PAIS = :1', [id_pais])
            if len(cursor.fetchall()) == 0:
                print('Nenhum País com este id')
                continue
        except ValueError:
            print('O id precisa ser um numero inteiro')
            continue
        except Exception as error:
            print(f'Erro ao buscar o id do país {error}')
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
    while True:
        suporte = criar_suporte()
        print(suporte)
        print('As informações estão corretas ?(digite apenas numeros)')
        match input('1 - sim\n'
                        '2 - não\n'):
            case '1':    
                try: 
                    query = f"""INSERT INTO SUPORTE (NOME_EMPRESA, NOME_PESSOA, SOBRENOME_PESSOA, DESCRICAO, ID_PAIS) VALUES (:1, :2, :3, :4, :5)"""
                    cursor.execute(query, [suporte["nome_empresa"], suporte["nome_pessoa"], suporte["sobrenome_pessoa"], suporte["descricao"], suporte["id_pais"]])
                    conn.commit()
                    print('Suporte cadastrado com sucesso')
                    atividade_do_site()
                    return
                except Exception as error:
                    print(f'Erro ao inserir suporte {error}')    
            case '2':
                print('Vamos cadastrar novamente')
                continue
            case _:
                print('Por favor escolha uma opção correta')

def atividade_do_site():
    """ Função responsável por salvar uma atividade do site toda vez que um suporte é cadastrado """
    try:
        pegar_id = """SELECT ID_SUPORTE FROM SUPORTE ORDER BY ID_SUPORTE DESC FETCH FIRST 1 ROWS ONLY"""
        cursor.execute(pegar_id)
        id_suporte = cursor.fetchall()[0][0]
        inserir_atividade = f"""INSERT INTO ATIVIDADE_DO_SITE(OPORTUNIDADE, DATA, ID_SUPORTE, ID_TESTE_GRATIS) VALUES ('N', SYSDATE, {id_suporte}, null)"""
        cursor.execute(inserir_atividade)
        conn.commit()
    except Exception as erro:
        print(f'Erro ao cadastrar atividade do site {erro}')   


def listar_suporte(filtro='all', parametro=''):
    """ Função responsável por listar todos os suportes do banco de dados """
    lista_suporte = []
    try:
        if filtro == 'all':
            cursor.execute("""SELECT * FROM SUPORTE ORDER BY ID_SUPORTE DESC""")
        elif filtro == 'id_suporte': 
            cursor.execute("""SELECT * FROM SUPORTE WHERE ID_SUPORTE = :1 ORDER BY ID_SUPORTE DESC""", [parametro])
        else:
            cursor.execute("""SELECT * FROM SUPORTE WHERE ID_PAIS = :1 ORDER BY ID_SUPORTE DESC""", [parametro])
        lista_suporte = cursor.fetchall()
        if len(lista_suporte) == 0:
            print('Nenhum suporte recuperado')
            return
        else:
            print('Suportes recuperados: ')
            for suporte in lista_suporte:
                print(f'id do suporte: {suporte[0]}')
                print(f'Nome da empresa: {suporte[1]}')
                print(f'Nome completa da pessoa: {suporte[2]} {suporte[3]}')
                print(f'Descrição da solicitação: {suporte[4]}')
                print(f'id do pais da solicitação: {suporte[5]}')
                print('-----------------------------------------------------')
            while True:
                match input('Deseja salvar essa consulta ? digite apenas numeros\n'
                '1 - Sim\n'
                '2 - Não\n'):
                    case '1':
                        nome_arquivo = input('Digite o nome do arquivo: ')
                        salvar_json(lista_suporte, nome_arquivo)
                        print('Retornando ao menu principal')
                        return
                    case '2':
                        print('Retornando ao menu principal')
                        return
                    case _:
                        print('Opção incorreta')
    except Exception as error:
        print(f'Erro ao se conectar no banco de dados: {error}')    
    

    """ Esta função lista todos os suportes por data """
    data = input('Digite a data que você deseja buscar: ') 
    

def atualizar_suporte():
    """ Função responsável por atualizar um suporte """
    try:
        id_suporte = int(input('Digite o id do suporte: '))
        verifica_suporte_cadastrado = f"""SELECT * FROM SUPORTE WHERE ID_SUPORTE = :1"""
        cursor.execute(verifica_suporte_cadastrado, [id_suporte])
        if len(cursor.fetchall()) == 0:
            print('Nenhum suporte cadastrado com esse id')
            return
        novo_suporte = criar_suporte()
        query = f"""UPDATE SUPORTE SET NOME_EMPRESA = :1,
                    NOME_PESSOA = :2, 
                    SOBRENOME_PESSOA = :3, DESCRICAO = :4, ID_PAIS = :5 WHERE ID_SUPORTE = :6"""
        
        cursor.execute(query, [novo_suporte['nome_empresa'], novo_suporte['nome_pessoa'], novo_suporte['sobrenome_pessoa'], novo_suporte['descricao'], novo_suporte['id_pais'], id_suporte])
        conn.commit()
        print(f'Suporte com o id {id_suporte} atualizado')
    except ValueError:
        print('o id do suporte precisa ser um numero inteiro')    
    except Exception as error:
        print(f'Erro ao atualizar suporte {error}')
    

def deletar_suporte():
    """ Função responsável por deletar um suporte """
    try:
        id_suporte = int(input('Digite o id do suporte: '))
        cursor.execute("""SELECT ID_SUPORTE FROM SUPORTE WHERE ID_SUPORTE = :1""", [id_suporte])
        if len(cursor.fetchall()) == 0:
            print('Sem nenhum suporte com este id')
            return
        deletar_suporte = f"""DELETE FROM SUPORTE WHERE ID_SUPORTE = :1"""
        deletar_atividade_do_site = f"""DELETE FROM ATIVIDADE_DO_SITE WHERE ID_SUPORTE = :1"""
        cursor.execute(deletar_atividade_do_site, [id_suporte])
        cursor.execute(deletar_suporte, [id_suporte])
        conn.commit()
        print(f'Suporte com o id {id_suporte} deletado')
    except ValueError:
        print('O id do suporte precisa ser um número inteiro')    
    except Exception as error:
        print(f'Erro ao deletar o suporte {error}')    


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
        print(f'Sucesso ao salvar as informações no arquivo : {nome_arquivo}.json')

while conexao:
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
