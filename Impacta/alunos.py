'''
CREATE TABLE TB_ALUNOSS
(ID INT AUTO_INCREMENT NOT NULL KEY,
ALUNOSS VARCHAR(30) NOT NULL UNIQUE);
'''


from flask import Flask, request
import mysql.connector
from mysql.connector import Error


app = Flask(__name__)

@app.route("/alunoss")
def todos_alunos():
    try:
        con = mysql.connector.connect(host='localhost',database='db_Alunos',user='root',password='Princesspeach@me2')

        consulta_sql = "select * from tb_alunoss"
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()
        return linhas
        
    except Error as e:
        print("Erro do BD:", e)
    finally:
        if (con.is_connected()):
            con.close()
            cursor.close()


@app.route("/alunoss", methods=["POST"])
def add_alunos():
    alunoss = request.args.get('cust')
    try:
        if alunoss is not None:
            con = mysql.connector.connect(host='localhost', database='db_Alunos', user='root', password='Princesspeach@me2')
            consulta_sql = "insert into tb_alunoss (alunoss) VALUE ('"+alunoss+"')"
            print(consulta_sql)
            cursor = con.cursor()
            cursor.execute(consulta_sql)
            con.commit()
            return "O aluno foi adicionado com sucesso!"
        else:
            return "Erro: valor 'cust' não fornecido na solicitação POST."
    except Error as e:
        print("Erro do BD:", e)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'con' in locals() and con.is_connected():
            con.close()



@app.route("/alunoss", methods=["DELETE"])
def delete_alunoss():
    alunoss = request.args.get('cust')
    id = request.args.get('id')
    if alunoss == None or alunoss == "":
        alunoss =""
    if id is None:
        id = "0"
    try:
        con = mysql.connector.connect(host='localhost',database='db_Alunos',user='root',password='Princesspeach@me2')
        cursor = con.cursor()
        consulta_sql = "delete from tb_alunoss where alunoss = '"+alunoss+"' or id = "+id
        cursor.execute(consulta_sql)
        linhas = todos_alunos()
        con.commit()
        count = 0
        for linha in linhas:
            if int(id) in linha or alunoss.lower() == linha[1].lower():
                cust = linha[1]
                count += 1
        if count == 1:
            return "A exclusão do aluno "+cust+" foi realizada com sucesso."
        else:
            return "Não foram encontrados registros do aluno na base de dados."
        
    
    except Error as e:
        print("Erro do BD:", e)
    finally:
        if (con.is_connected()):
            con.close()
            cursor.close()


if __name__ == '__main__':
    app.run(debug=True, port="5000")
