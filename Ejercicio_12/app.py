from flask import Flask, render_template
from models.database import db
from routes.api import api_bp #Librerias que usamos 

#inicio flask

app = Flask(__name__)

#Configuro mi conexion a SQLlite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventario.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Vincular db con la app
db.init_app(app)

#Registrar blueprint
app.register_blueprint(api_bp)

#Crear mis tablas
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html') #Si todo funciona lo manda a la pagina de incio

if __name__== '__main__':
    app.run(debug=True)