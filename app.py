from flask import Flask, render_template, request, jsonify, flash, session, redirect, url_for
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = "versatilsoftwares123"
CORS(app)

host = "0.0.0.0"
port = 8000
debug = True




@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('venda.html', title='Vendas')

@app.route("/index", methods=['GET', 'POST'])
def retornar():
    return redirect(url_for("index"))

@app.route("/seleciona-cliente", methods=['GET', 'POST'])
def select_cliente():
    return render_template('select_cliente.html', title='Clientes')

@app.route("/seleciona-produto", methods=['GET', 'POST'])
def select_produto():
    return render_template('select_produto.html', title='Produtos')

if __name__ == __name__:
    app.run(host=host, port=port, debug=debug)
