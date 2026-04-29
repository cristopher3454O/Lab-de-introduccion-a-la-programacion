from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)
DB_PATH = 'inventario_db.sqlite'

CARRITO = []
# Iniciamos con None para que no haya falsos positivos
ULTIMO_EVENTO = {"tipo": None, "codigo": None}

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def admin():
    return render_template('admin.html')

@app.route('/scanner')
def scanner_view():
    return render_template('scanner.html')

@app.route('/api/escanear', methods=['POST'])
def api_escanear():
    global ULTIMO_EVENTO, CARRITO
    data = request.json
    cod = data.get('codigo')
    
    if not cod:
        return jsonify({"status": "error", "message": "No code"})

    with get_db() as conn:
        # Buscamos si ya existe
        prod = conn.execute('SELECT * FROM productos WHERE codigo = ?', (cod,)).fetchone()
        
        if prod:
            # PRODUCTO CONOCIDO
            item = {"codigo": prod['codigo'], "nombre": prod['nombre'], "precio": prod['precio']}
            CARRITO.append(item)
            ULTIMO_EVENTO = {"tipo": "agregado", "codigo": cod}
            print(f"DEBUG: {prod['nombre']} agregado al carrito")
        else:
            # PRODUCTO NUEVO - Aquí disparamos la señal para el modal
            ULTIMO_EVENTO = {"tipo": "nuevo", "codigo": cod}
            print(f"DEBUG: Código nuevo detectado: {cod}")
            
    return jsonify({"status": "ok"})

@app.route('/api/sync')
def sync():
    global ULTIMO_EVENTO
    # Mandamos la copia de los datos actuales
    data = {
        "lista_productos": CARRITO,
        "evento_tipo": ULTIMO_EVENTO["tipo"],
        "evento_codigo": ULTIMO_EVENTO["codigo"]
    }
    # IMPORTANTE: Solo limpiamos el evento después de que la lap lo lea
    if ULTIMO_EVENTO["tipo"] is not None:
        ULTIMO_EVENTO = {"tipo": None, "codigo": None}
        
    return jsonify(data)

@app.route('/api/registrar', methods=['POST'])
def registrar():
    data = request.json
    try:
        # Tomamos la cantidad que mandaste desde la laptop
        cantidad_inicial = data.get('cantidad', 1) 
        
        with get_db() as conn:
            conn.execute('''INSERT INTO productos (codigo, nombre, sku, precio, cantidad) 
                         VALUES (?, ?, ?, ?, ?)''', 
                         (data['codigo'], data['nombre'], data['sku'], data['precio'], cantidad_inicial))
            conn.commit()
        
        # Lo agregamos al carrito visual
        CARRITO.append({"codigo": data['codigo'], "nombre": data['nombre'], "precio": data['precio']})
        return jsonify({"status": "ok"})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"status": "error"}), 500
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False, ssl_context='adhoc')