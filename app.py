# import do framework
# import do render_template para a leitura HTML
# request para captura de dados

from flask import Flask, render_template, required
# biblioteca para criar conexão com mysql
import mysql.connector

bd_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'escola',
    'database': 'cadastro1'
}