import mysql.connector
from mysql.connector import Error

try:
    con = mysql.connector.connect(host='localhost',database='db_Alunos',user='root',password='Princesspeach@me2')

    nome = 'João'
    sobrenome = 'da Silva'
    turma = 'ADS2Y'

    consulta_sql = "INSERT INTO tb_aluno VALUES ('"+nome+"', '"+sobrenome+"', '"+turma+"' )"
    print(consulta_sql)
    cursor = con.cursor()
    cursor.execute(consulta_sql)

    con.commit()

except Error as e:
    print('Erro ao acessar tabela MySQL', e)
finally:
    if (con.is_connected()):
        con.close()
        cursor.close()
        print('Conexão ao MySQL encerrada.')