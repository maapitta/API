from flask import Flask, request
import http.client


app = Flask(__name__)

@app.route("/")
def todos_alunos():
    try:
        print("teste")
        conn = http.client.HTTPConnection("127.0.0.1", 5000)
        conn.request("GET", "/alunos")
        response = conn.getresponse()
        return response.read().decode("utf-8")
    except:
        return "Houve uma falha na comunicação com a API externa.", 502

@app.route("/", methods=["POST"])
def add_alunos():
    try:
        alunos = request.args.get('cust')
        conn = http.client.HTTPConnection("127.0.0.1", 5000)
        conn.request("POST", "/clientes?cust=" + alunos)
        response = conn.getresponse()
        return response.read().decode("utf-8")
    except:
        return "Não foi possível estabelecer conexão com a API externa.", 502

@app.route("/", methods=["DELETE"])
def delete_alunos():
    try:    
        alunos = request.args.get('cust')
        id = request.args.get('id')
        if alunos == None:
            alunos = "-----"
        if id is None:
            id = "0"
        conn = http.client.HTTPConnection("127.0.0.1", 5000)
        conn.request("DELETE", "/alunos?cust=" + alunos + "&id=" + id)
        response = conn.getresponse()
        return response.read().decode("utf-8")
    except:
        return "A comunicação com a API externa falhou.", 502


if __name__ == '__main__':
    app.run(debug=True, port="5001")
