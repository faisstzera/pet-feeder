from flask import Flask, g, render_template, session, request
from flask_cors import CORS
from flask_login import LoginManager
login_manager = LoginManager()


from controllers.auth_controller import auth
from controllers.base_controller import base
from controllers.billing_controller import billing
from controllers.iot_controller import iot
from controllers.payment_controller import payment
from controllers.people_controller import people
from controllers.product_controller import product
from controllers.ticket_controller import ticket

app = Flask(__name__, template_folder="./views/", static_folder="./static/")

CORS(app, resources={r'/*': {'origins': '*'}})

app.register_blueprint(base, url_prefix='/base')

app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(billing, url_prefix='/billing')
app.register_blueprint(payment, url_prefix='/payment')
app.register_blueprint(people, url_prefix='/people')
app.register_blueprint(product, url_prefix='/product')
app.register_blueprint(ticket, url_prefix='/ticket')
app.register_blueprint(iot, url_prefix='/iot')

login_manager = LoginManager()
login_manager.init_app(app)

# Renderizar a página inicial

usuarios = {}


@app.route('/')
def index():
    return render_template("home.html")


@app.route('/people', methods=['POST', 'GET'])
def employees():
    return render_template("home.html")

# Função de login
login_manager.login_view = 'login'

@app.route('/auth', methods=['POST'])
def login():
    info = json.loads(request.data)
    username = info.get('username', 'guest')
    password = info.get('password', '') 
    user = User.objects(name=username,
                        password=password).first()
    if user:
        login_user(user)
        return jsonify(user.to_json())
    else:
        return jsonify({"status": 401,
                        "reason": "Username or Password Error"})



if __name__ == "__main__":
    app.run(debug=True)
