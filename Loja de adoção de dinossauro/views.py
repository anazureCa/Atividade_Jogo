from site import app
from flask import render_template


#rotas
@app.route("/")
def main():
    return render_template('main.html')

@app.route("/Dinossauros")
def main():
    return render_template('Cadastro_dinossauros.html')

@app.route("/Funcionarios")
def main():
    return render_template('Cadastro_funcionarios.html')

@app.route("/Financeiro")
def main():
    return render_template('financeiro.html')

@app.route("/Plano-Saude")
def main():
    return render_template('plano_saude.html')
