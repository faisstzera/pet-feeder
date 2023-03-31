import json

from flask import Blueprint, redirect, render_template, request, url_for

product = Blueprint("product", __name__, template_folder='./views/', static_folder='./static/', root_path="./")

produtos_a_registrar = [1000,2000,3000,4000,5000]


@product.route("/")
def products_index():
    return render_template("/product/product_index.html")

@product.route("/register_product")
def register_product():
    if request.method['POST']:
        numero_cadastro = request.form['numero_cadastro']
    
    if numero_cadastro in produtos_a_registrar:
        with open('/controllers/registered_products.json', 'r') as file:
            json_data = json.load(file)
            json_data['produto'] = numero_cadastro
            json_data['ativo']= False
        with open('registered_products.json', 'w') as file:
            json.dump(json_data, file, indent=2)
        
        return json_data, 200
        

    return "Produto não encontrado!", 400

