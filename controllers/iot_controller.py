import json

from flask import Blueprint, redirect, render_template, request, url_for

iot = Blueprint("iot", __name__, template_folder='./views/',
                static_folder='./static/', root_path="./")


@iot.route("/")
def iot_index():
    # Opening JSON file
    json_file = open('registered_products.json')
    produtos_registrados = json_file.read()
    json_file.close()

    # convertendo a string JSON em uma lista de dicionários Python
    produtos_registrados = json.loads(produtos_registrados)

    # removendo os produtos inativos
    produtos_ativos = []
    for produto in produtos_registrados:
        if produto['ativo']:
            produtos_ativos.append(produto)

    print(produtos_ativos)

    # ler dados do json e retornar os produtos registrados
    return render_template("/iot/iot_index.html", produtos_registrados=produtos_ativos)
