from flask import Blueprint, jsonify, request
from models.database import db, Producto #Importe db para guardar y producto para buscar

#Definir el blueprint
api_bp = Blueprint('api', __name__)

#Ruta para la consulta get
@api_bp.route('/api/producto/<codigo>', methods=['GET'])
def obtener_producto(codigo):
    #Buscar productos en la base de datos
    producto = Producto.query.filter_by(codigo_barras=codigo).first()

    if producto:
        #Si existe devolvemos datos en formato JSNO
        return jsonify({
            "existe":True,
            "nombre": producto.nombre,
            "precio": producto.precio
        }) , 200
    else: 
        #Si no existe, devolvemos un mensaje de error y codigo 404
        return jsonify({
            "existe": False,
            "mensaje": "Producto no encontrado "
        }) ,404
    
#Ruta para registrar productos
@api_bp.route('/api/producto/registrar', methods=['POST'])
def registrar_producto():
    #Recibir datos enviados desde el fronted
    datos = request.get_json()

    #Creamos un nuevo objeto del modelo producto
    nuevo_producto = Producto(
        codigo_barras=datos['codigo'],
        nombre=datos['nombre'],
        precio=datos['precio']
    )
    #Agregamos a la sesion y guardamos en la base de datos
    db.session.add(nuevo_producto)
    db.session.commit()

    return jsonify({"mensaje": "Producto registrado con exito"}, 201)
