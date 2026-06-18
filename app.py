# import do framework
# import do render_template para a leitura HTML
# request para captura de dados

from flask import Flask, render_template, request
# biblioteca para criar conexão com mysql
import mysql.connector

app = Flask(__name__)

bd_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'escola',
    'database': 'cadastro1'
}

# Criação de rota para o arquivo HTML principal
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastrar', methods=['POST'])
def criar_cadastro():
    cpf = request.form['cpf']
    primeiro_nome = request.form['primeiro_nome']
    sobrenome = request.form['sobrenome']
    idade = request.form['idade']

    # Criando a conexão com o banco de dados
    conectar = mysql.connector.connect(**bd_config)

    # Leva as instruções do SQL até o Python
    transporte = conectar.cursor()

    query = "INSERT INTO cliente1 (CPF, PRIMEIRO_NOME, SOBRENOME, IDADE) VALUES (%s, %s, %s, %s)"