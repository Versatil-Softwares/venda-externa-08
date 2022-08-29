from flask import Flask, render_template, request, jsonify, flash, session, redirect, url_for
from flask_cors import CORS
from app import app


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

@app.route("/cliente-detalhe", methods=['GET', 'POST'])
def detalhe_clinete():
    return render_template('detalhe_cliente.html', title='Cliente')

@app.route("/produto-detalhe", methods=['GET', 'POST'])
def detalhe_produto():
    return render_template('detalhe_produto.html', title='Produto')

@app.route("/carrinho", methods=['GET', 'POST'])
def carrinho():
    return render_template('carrinho.html', title='Carrinho')