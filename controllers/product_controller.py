from flask import Blueprint, render_template,redirect,url_for, request

product = Blueprint("product", __name__, template_folder='./views/', static_folder='./static/', root_path="./")

produtos_a_registrar = [1000,2000,3000,4000,5000]
produtos_registrados = []


@product.route("/")
def products_index():
    return render_template("/product/product_index.html")

@product.route("/product")
def register_product():
    if request.method['POST']:
        numero_cadastro = request.form['numero_cadastro']

        if numero_cadastro in produtos_a_registrar:
            produtos_registrados.append(numero_cadastro)
            produtos_a_registrar.remove(numero_cadastro)
            return "Produto ativado!", 200
        else:
            return "Produto não encontrado", 400

