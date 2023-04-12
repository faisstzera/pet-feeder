from flask import Blueprint, redirect, render_template, url_for

base = Blueprint("base", __name__, template_folder="./views/", static_folder='./static/', root_path="./")

@base.route("/")
def base_index():
    return render_template("base.html")


@base.route('/form_example')
def base_form_example():
    return render_template("base/view_example.html")