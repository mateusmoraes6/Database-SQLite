import sqlite3

class DDLSQLite:
    def _conectar(self, nome_banco):
        nome_banco += '.db'
        conn = sqlite3.connect(nome_banco)
        return conn
    
    def criar_banco_de_dados(self, nome_banco):
        nome_banco += '.db'
        sqlite3.connect(nome_banco).close()
        print(f"O banco de dados {nome_banco} foi criado com sucesso!")
        return None
    
    def criar_tabela(self, nome_banco, ddl_create):
        conn = self._conectar(nome_banco)
        cursor = conn.cursor()
        cursor.execute(ddl_create)
        cursor.close()
        conn.close()
        print(f"Tabela criada com sucesso!")
        
    def apagar_tabela(self, nome_banco, tabela):
        conn = self._conectar(nome_banco)
        cursor = conn.cursor()
        cursor.execute(f"DROP TABLE {tabela}")
        cursor.close()
        conn.close()
        print(f"A tabela {tabela} foi excluída com sucesso!")
        return None
