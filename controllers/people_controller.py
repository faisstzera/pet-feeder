import json

from flask import Blueprint, redirect, render_template, request, url_for

people = Blueprint("people", __name__, template_folder='./views/', static_folder='./static/', root_path="./")

@people.route("/")
def people_index():
    json_file = open('registered_people.json')
    pessoas_registradas = json.load(json_file)
    for i in pessoas_registradas['active']:
        print(i)
    json_file.close()
    return render_template("/people/people_index.html", pessoas_registradas = pessoas_registradas)

@people.route("/people", methods=['GET', 'POST'])
def register_people():
    
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
            
            return json_data, 200
        else:
            return('Usuário Já cadastrado', 400)