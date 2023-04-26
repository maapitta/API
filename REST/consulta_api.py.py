from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def consulta():
    informacoes = {'nome': 'Amalia', 'faculdade': 'Impacta', 'matricula': '2200519', 'AC': '02', 'turma': 'ADS3B'}

    return jsonify(informacoes)

if __name__ == '__main__':
    app.run()
