from flask import Blueprint, render_template,redirect,url_for,request
from auth_controller import registered_users

people = Blueprint("people", __name__, template_folder='./views/', static_folder='./static/', root_path="./")

@people.route("/")
def people_index():
    return render_template("/people/people_index.html")

@people.route("/people", methods=['GET', 'POST'])
def get_people():
    
    if request.method['GET']:  
        return registered_users, 200
    
    elif request.method['POST']:
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