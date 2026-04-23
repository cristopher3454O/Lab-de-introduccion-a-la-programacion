import sqlite3
from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)
DB_NAME = 'pos_pro.db'
shared_cart = []

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS products 
                        (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                         barcode TEXT UNIQUE, name TEXT, price REAL, stock INTEGER)''')
        conn.commit()

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>POS Sistema</title>
    <script src="https://unpkg.com/html5-qrcode"></script>
    <style>
        :root { --primary: #2c3e50; --accent: #27ae60; }
        body { font-family: sans-serif; margin: 0; background: #f0f2f5; }
        .container { display: flex; flex-direction: column; height: 100vh; }
        
        /* Layout Responsivo */
        @media (min-width: 768px) { .container { flex-direction: row; } }
        
        .panel { flex: 1; padding: 20px; overflow-y: auto; }
        .card { background: white; padding: 20px; border-radius: 10px; box-shadow: 0 2px 5px #ccc; margin-bottom: 20px; }
        
        button { width: 100%; padding: 15px; border: none; border-radius: 8px; color: white; font-size: 16px; margin: 5px 0; cursor: pointer; }
        .btn-pos { background: var(--primary); }
        .btn-cam { background: var(--accent); }
        
        #reader { width: 100%; border-radius: 8px; background: #eee; }
        input { width: 100%; padding: 15px; margin: 10px 0; border: 1px solid #ccc; box-sizing: border-box; border-radius: 8px; }
    </style>
</head>
<body>
<div class="container">
    <div class="panel">
        <div class="card">
            <h3>🛒 Punto de Venta (Scanner)</h3>
            <div id="reader"></div>
            <button class="btn-cam" onclick="startScanner('pos')">ACTIVAR CÁMARA</button>
            <button class="btn-pos" onclick="stopScanner()">DETENER CÁMARA</button>
        </div>
        <div class="card">
            <h3>Carrito Sincronizado</h3>
            <div id="display-cart"></div>
            <h2 id="total">Total: $0.00</h2>
            <button style="background: #e74c3c;" onclick="clearCart()">LIMPIAR</button>
        </div>
    </div>

    <div class="panel">
        <div class="card">
            <h3>➕ Registrar Producto</h3>
            <div id="reader_admin"></div>
            <button class="btn-cam" onclick="startScanner('admin')">ESCANEAR CÓDIGO NUEVO</button>
            <input type="text" id="p_barcode" placeholder="Código de barras">
            <input type="text" id="p_name" placeholder="Nombre">
            <input type="number" id="p_price" placeholder="Precio">
            <button class="btn-pos" onclick="saveProduct()">GUARDAR</button>
        </div>
    </div>
</div>

<script>
    let scanner = null;

    function startScanner(mode) {
        const id = (mode === 'pos') ? "reader" : "reader_admin";
        scanner = new Html5Qrcode(id);
        scanner.start(
            { facingMode: "environment" }, 
            { fps: 10, qrbox: 200 },
            (decodedText) => {
                if(mode === 'pos') {
                    fetch('/api/add_to_cart', {method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify({code: decodedText})});
                } else {
                    document.getElementById('p_barcode').value = decodedText;
                }
                stopScanner();
            }
        ).catch(err => alert("Permiso denegado o error de cámara. Intenta usar HTTPS o Chrome."));
    }

    function stopScanner() { if(scanner) scanner.stop().catch(err => console.log(err)); }

    async function fetchCart() {
        const res = await fetch('/api/get_cart');
        const data = await res.json();
        document.getElementById('display-cart').innerHTML = data.items.map(i => `<div>${i.name} - $${i.price}</div>`).join('');
        document.getElementById('total').innerText = 'Total: $' + data.total.toFixed(2);
    }

    async function saveProduct() {
        const p = {barcode: document.getElementById('p_barcode').value, name: document.getElementById('p_name').value, price: document.getElementById('p_price').value};
        await fetch('/api/add_product', {method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify(p)});
        alert('Guardado');
    }

    async function clearCart() { await fetch('/api/clear', {method:'POST'}); }

    setInterval(fetchCart, 1000);
</script>
</body>
</html>
'''

# --- API ENDPOINTS ---
@app.route('/')
def index(): return render_template_string(HTML_TEMPLATE)

@app.route('/api/get_cart')
def get_cart():
    total = sum(item['price'] for item in shared_cart)
    return jsonify({'items': shared_cart, 'total': total})

@app.route('/api/add_to_cart', methods=['POST'])
def add_to_cart():
    code = request.json['code']
    conn = sqlite3.connect(DB_NAME)
    prod = conn.execute('SELECT * FROM products WHERE barcode=?', (code,)).fetchone()
    conn.close()
    if prod: shared_cart.append({'name': prod[2], 'price': prod[3]})
    return jsonify({'status':'ok'})

@app.route('/api/add_product', methods=['POST'])
def add_prod():
    d = request.json
    conn = sqlite3.connect(DB_NAME)
    conn.execute('INSERT OR IGNORE INTO products (barcode, name, price) VALUES (?,?,?)', (d['barcode'], d['name'], d['price']))
    conn.commit(); conn.close()
    return jsonify({'status':'ok'})

@app.route('/api/clear', methods=['POST'])
def clear(): shared_cart.clear(); return jsonify({'status':'ok'})

if __name__ == '__main__':
    init_db()
    # Ejecuta en 0.0.0.0 para acceso local
    app.run(debug=True, host='0.0.0.0', port=5000)