import sqlite3

def conectar_banco():
    conexao = sqlite3.connect("bancodedados")
    return conexao


def criar_tabelas():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS filmes
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       titulo TEXT, diretor TEXT, ano_publicacao INT)''')
    conexao.commit()
    conexao.close()

def adicionar_filme(titulo, diretor, ano_publicacao):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''INSERT INTO filmes (titulo, diretor, ano_publicacao)
                   VALUES (?,?,?)''', (titulo, diretor, ano_publicacao))
    conexao.commit()
    cursor.close()
    return True

def editar_filme(titulo, diretor, ano_publicacao, id):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute(''' UPDATE filmes SET titulo = ?, diretor = ?, ano_publicacao = ? WHERE id = ?''', (titulo, diretor, ano_publicacao, id))
    conexao.commit()
    cursor.close()
    return True

def excluir_filme(id):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute(''' DELETE FROM filmes WHERE id = ?''', (id,))
    conexao.commit()
    conexao.close()
    return True

def filmes_2010():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''SELECT * FROM filmes WHERE ano_publicacao >= 2010''')
    resultados = cursor.fetchall()
    conexao.close()
    return resultados


if __name__ == '__main__':
    criar_tabelas()
    print("Hello World!")
    adicionar_filme('titulo', 'diretor', 2011)
    editar_filme('velozes e furiosos', 'Rob Cohen', 2001, 1)
    excluir_filme(2)

    filmes = filmes_2010()
    if filmes:
        print("Filmes de 2010 ou mais recentes:")
        for filme in filmes:
            print(f"ID: {filme[0]}, Título: {filme[1]}, Diretor: {filme[2]}, Ano: {filme[3]}")
    else:
        print("Nenhum filme encontrado.")