# pip install sqlalchemy

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


# Padrão para a construção do banco de dados --------------------------------------
engine = create_engine('sqlite:///atividades.db')
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base() # Isso é default do sqlalchemy
Base.query = db_session.query_property()
#-----------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------
# No bd haverá pessoas com os campos id, nome e idade
class Pessoas(Base):
    __tablename__='pessoas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    idade = Column(Integer)

    # Ao fazer uma solicitação de busca será retornado o nome da pessoa
    def __repr__(self):
        return '<Pessoa {}>'.format(self.nome)

    # Para commitar (salvar o novo registro no bd)
    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()
#-----------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------
# Pessoas possuirão Atividades compostas por id, nome e uma foreign key pessoa_id
class Atividades(Base):
    __tablename__='atividades'
    id = Column(Integer, primary_key=True)
    nome = Column(String(80))
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'))
    pessoa = relationship("Pessoas")

    def __repr__(self):
        return '<Atividades {}>'.format(self.nome)

    # Método para commitar (salvar o novo registro no bd)
    def save(self):
        db_session.add(self)
        db_session.commit()
    # Método para deletar uma atividade do bd
    def delete(self):
        db_session.delete(self)
        db_session.commit()
#-----------------------------------------------------------------------------------

class Usuarios(Base):
    __tablename__='usuarios'
    id = Column(Integer, primary_key=True)
    login = Column(String(20), unique=True)
    senha = Column(String(20))

    def __repr__(self):
        return '<Usuario {}>'.format(self.login)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


#-----------------------------------------------------------------------------------
# Inicia o banco de dados (cria o arquivo "atividades.db")
def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()
#-----------------------------------------------------------------------------------
