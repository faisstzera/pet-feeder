import json

from flask import Blueprint, redirect, render_template, request, url_for

auth = Blueprint("auth", __name__, template_folder="./views/", static_folder='./static/', root_path="./")


@auth.route("/")
def auth_index():
    return render_template("auth/auth_index.html")

@auth.route('/auth', methods=['POST','GET'])
def login():
    
    # Registrar o usuário
    if request.method['POST']:

        usuario = request.form['usuario']
        
        with open('registered_people.json', 'r') as file:
            json_data = json.load(file)

        if usuario in json_data:
            usuario_a_registrar= {}

            senha = request.form['senha']
            nome = request.form['nome']
            email = request.form['email']

            usuario_a_registrar['usuario'] = usuario
            usuario_a_registrar['senha'] = senha
            usuario_a_registrar['nome'] = nome
            usuario_a_registrar['email'] = email

            with open('registered_people.json', 'w') as file:
                json.dump(json_data, file, indent=2)
            
            return json_data,200
        else:
            return('Usuário Já cadastrado', 400)
                
    # Fazer login
    elif request.method['GET']:
        usuario_request = request.form['usuario']
        senha_request = request.form['senha']

        with open('registered_people.json', 'r') as file:
            json_data = json.load(file)

        if json_data['usuario'] == usuario_request and json_data['senha'] == senha_request:
            return redirect('/', code=200)

        else:
            return "Senha Incorreta", 403

