from flask_sqlalchemy import SQLAlchemy

# 1. Creamos la instancia de la base de datos
db = SQLAlchemy()

# 2. Definimos la clase que representa la tabla
class Producto(db.Model):
    # 3. ID único para cada fila
    id = db.Column(db.Integer, primary_key=True)
    
    # 4. Código de barras: debe ser único y lo indexamos para búsquedas rápidas
    codigo_barras = db.Column(db.String(50), unique=True, nullable=False, index=True)
    
    # 5. Nombre y precio dek productos
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    
    # 6. Representación para depuración
    def __repr__(self):
        return f'<Producto {self.nombre}>'