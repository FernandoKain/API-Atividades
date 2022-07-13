from models import Pessoas, Usuarios

# Método para inserir pessoas no bd
def insere_pessoas():
    # id não precisa pois é a primary key, então será feito automaticamente
    pessoa = Pessoas(nome='Fernando', idade=42)
    #pessoa = Pessoas(nome='Terezinha', idade=42)
    print(pessoa)
    pessoa.save() # Método descrito em models para commitar a inserção no bd

# Método para realizar consultas no bd
def consulta():
    pessoa = Pessoas.query.all()
    for i in pessoa:
        print('Consulta por tuplas:', i.nome)
    print('Todos os registros do bd:', pessoa)

# Método para realizar consultas filtradas no bd
def consulta_filtrada():
    pessoa = Pessoas.query.filter_by(nome='Fernando')
    for i in pessoa:
        print('Consulta filtrada:', i.nome)

# Método para realizar consulta filtrada pela idade no bd
def consulta_pela_idade():
    pessoa = Pessoas.query.filter_by(nome='Fernando').first()
    print('Consulta por idade:', pessoa.nome, pessoa.idade)
    pessoa = Pessoas.query.filter_by(nome='Terezinha').first()
    print('Consulta por idade:', pessoa.nome, pessoa.idade)

# Método para alterar um atributo de um registro no bd
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Terezinha').first()
    pessoa.idade = 21
    pessoa.save()

# Método para excluir um registro do bd
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Fernando').first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == '__main__':
    insere_usuario('Fernando', '1234')
    insere_usuario('Fernanda', '1234')
    consulta_todos_usuarios()
    #insere_pessoas()
    #consulta()
    #consulta_filtrada()
    #consulta_pela_idade()
    #altera_pessoa()
    #exclui_pessoa()