from flask import Flask, render_template, jsonify

app = Flask(__name__)

VAGAS = [{
  'id': 1,
  'titulo': 'Analista de Dados',
  'localidade': 'RJ, Brasil',
  'salario': 'R$ 5000.00'
}, {
  'id': 2,
  'titulo': 'Dev FrontEnd',
  'localidade': 'PR, Brasil',
  'salario': 'R$ 3000.00'
}, {
  'id': 3,
  'titulo': 'Cientista de Dados',
  'localidade': 'SP, Brasil',
  'salario': 'R$ 4000.00'
}, {
  'id': 4,
  'titulo': 'Dev BackEnd',
  'localidade': 'RJ, Brasil',
  'salario': 'R$ 5500.00'
}, {
  'id': 5,
  'titulo': 'Estatistico',
  'localidade': 'SP, Brasil',
  'salario': 'R$ 3400.00'
}]


@app.route('/')
def page_home():
  return render_template('home.html', vagas=VAGAS)


@app.route('/vagas')
def lista_vagas():
  return jsonify(VAGAS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
