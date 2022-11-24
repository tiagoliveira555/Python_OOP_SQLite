from model.Pessoa import Pessoa
from database.Database import Database
from dao.PessoaDAO import PessoaDAO

p1 = Pessoa(1, 'Tiago')

print(p1)
print('-' * 10)

db = Database()

pessoas = PessoaDAO(db.conexao, db.cursor).getAll(True)

for pessoa in pessoas:
  print(pessoa)
