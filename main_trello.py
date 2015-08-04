from trollop import *

key = u'9cd60a9e9eab461420670948ad742fbb'
auth = u'e595b1844450a51fd0ce615d7a295fe5cb669ba104aaf2dbb010d1d27d626283'
conn = TrelloConnection(api_key=key, oauth_token=auth)
cod_board = u'dC5QL1a6'

class Manipula_Trello:
    '''
    Esta eh a classe designada para a manipulacao da api do trello.
    Tem por objetivos tratar da listagens de pessoas participantes de tarefas, das tarefas e tempo.
    '''


    def Conecta_Usuario_id(self, key, OAuth):

        '''
        Neste metodo eh realizada a conexao com a conta do usuario.
        Sera usada a key da conta do usuario e OAuth que eh uma chave de permissao para o servidor.
        '''
        conn = TrelloConnection(key, OAuth)
        return conn

    def Seleciona__Boards_Pessoa(self,conector):
        '''Metodo retorna os boards para cada conexao'''
        tamanho = len(conector.me.boards)
        while tamanho>0:
            print conector.me.boards[tamanho-1]
            tamanho=tamanho-1

    def Retorna_Com_id(self,conector,id):
        usuario_id = str(id)
        usuario = conector.get_member(usuario_id)
        return usuario.fullname

    def lista_de_pessoas_nos_boards(self, conector,border_id):
        '''O metodo pegara os participantes do border, criara uma lista dos mesmos, sao os participantes de uma tarefa'''
        adapta_id = str(border_id)
        Lista_Pessoas_Board = conector.get_board(adapta_id)
        tamanho = len(Lista_Pessoas_Board)
        while tamanho>0:
            i=tamanho-1
            tamanho = tamanho-1
            return Lista_Pessoas_Board[i]


