from flask import Blueprint, render_template, redirect, url_for, request
import json

auth = Blueprint("auth", __name__, template_folder="./views/", static_folder='./static/', root_path="./")

global registered_users
registered_users = []


@auth.route("/")
def auth_index():
    return render_template("auth/auth_index.html")

@auth.route('/auth', methods=['POST','GET'])
def login():
    
    # Registrar o usuário
    if request.method['POST']:
        usuario = request.form['usuario']
        if not any(dicionario['usuario'] == usuario for dicionario in registered_users):
            return "Record not found", 400
            
        else:
            usuario_a_registrar= {}

            senha = request.form['senha']
            nome = request.form['nome']
            email = request.form['email']

            usuario_a_registrar [usuario] = usuario
            usuario_a_registrar [senha] = senha
            usuario_a_registrar [nome] = nome
            usuario_a_registrar [email] = email

            registered_users.append(usuario_a_registrar)

            return "Usuário cadastrado!", 200
            
        

    # Fazer login
    elif request.method['GET']:
        usuario_request = request.form['usuario']
        senha_request = request.form['senha']

        dict_usuario = list(filter(lambda person: person['usuario'] == usuario_request, registered_users))[0]

        if len(dict_usuario)>0:
                if (dict_usuario[usuario] == usuario_request) and (dict_usuario[senha] == senha_request):
                    return redirect('/', 200)
                else:
                    return "Senha não cadastrada!", 400

        else:
            return "Usuário já cadastrado", 400

