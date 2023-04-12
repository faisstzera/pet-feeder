import json
import os

from flask import (Blueprint, Response, redirect, render_template, request,
                   url_for)

auth = Blueprint("auth", __name__, template_folder="./views/",
                 static_folder='./static/', root_path="./")


@auth.route("/")
def auth_index():
    return render_template("auth/auth_index.html")


@auth.route('/login', methods=['POST', 'GET'])
def login():

    # Registrar o usuário
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']
        nome = request.form['nome']
        email = request.form['email']

        try:
            with open('registered_users.json', 'r') as file:
                json_data = json.load(file)
            print(json_data)
        except FileNotFoundError:
            json_data = {}

        if usuario not in json_data:
            usuario_a_registrar = {}
            usuario_a_registrar['usuario'] = usuario
            usuario_a_registrar['senha'] = senha
            usuario_a_registrar['nome'] = nome
            usuario_a_registrar['email'] = email

            json_data[usuario] = usuario_a_registrar

            with open('registered_users.json', 'w') as file:
                json.dump(json_data, file, indent=2)

            return Response('', 200)
        else:
            return Response('', 400)

    # Fazer login
    elif request.method == 'GET':
        usuario_request = request.form['usuario']
        senha_request = request.form['senha']

        try:
            with open('registered_users.json', 'r') as file:
                json_data = json.load(file)
        except FileNotFoundError:
            json_data = {}

        if usuario_request in json_data and json_data[usuario_request]['senha'] == senha_request:
            return redirect('/', code=200)
        else:
            return Response('', 500)
    else:
        return Response('', 404)
