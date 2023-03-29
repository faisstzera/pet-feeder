from flask import Blueprint, render_template,redirect,url_for, request
from product_controller import produtos_registrados

iot = Blueprint("iot", __name__, template_folder = './views/', static_folder='./static/', root_path="./")

@iot.route("/")
def iot_index():
    return render_template("/iot/iot_index.html")

@iot.route("/iot", methods=['GET'])
def iot_index():
    
    if request.method['GET']:
        return produtos_registrados, 200