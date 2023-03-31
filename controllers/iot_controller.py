import json

from flask import Blueprint, redirect, render_template, request, url_for

iot = Blueprint("iot", __name__, template_folder = './views/', static_folder='./static/', root_path="./")


@iot.route("/")
def iot_index():
    # Opening JSON file
    json_file = open('registered_products.json')
    produtos_registrados = json.load(json_file)
    for i in produtos_registrados['active']:
        print(i)
    json_file.close()

    # ler dados do json e retornar os produtos registrados
    return render_template("/iot/iot_index.html", produtos_registrados=produtos_registrados)
