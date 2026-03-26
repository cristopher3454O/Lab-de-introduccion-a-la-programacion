from flask import Flask, render_template_string, request, redirect, url_for, session

app = Flask(__name__)
# La secret_key es obligatoria para usar session
app.secret_key = "clave_secreta_2026"

# --- CLASE POO PARA VALIDACIÓN ---
class Admin:
    def __init__(self):
        self.user = "admin"
        self.password = "admin2026"

    def verificar(self, u, p):
        return u == self.user and p == self.password

auth_manager = Admin()

# --- PLANTILLA HTML (Separada para evitar errores de sintaxis) ---
HTML_BASE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Sistema de Cards</title>
    <style>
        body { font-family: 'Segoe UI', sans-serif; background: #f1f5f9; display: flex; flex-direction: column; align-items: center; margin: 0; }
        .container { display: flex; gap: 20px; padding: 50px; flex-wrap: wrap; justify-content: center; }
        .card { background: white; width: 280px; border-radius: 15px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); overflow: hidden; text-align: center; border: 1px solid #e2e8f0; }
        .card img { width: 100%; height: 150px; object-fit: cover; }
        .card-body { padding: 20px; }
        .btn { background: #2563eb; color: white; padding: 10px 20px; text-decoration: none; border-radius: 8px; display: inline-block; font-weight: bold; border: none; cursor: pointer; }
        .login-card { background: white; padding: 40px; border-radius: 15px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); margin-top: 100px; width: 320px; text-align: center; }
        input { width: 100%; padding: 12px; margin: 10px 0; border: 1px solid #cbd5e1; border-radius: 8px; box-sizing: border-box; }
    </style>
</head>
<body>

    {# Usamos session directamente, Flask lo pasa automáticamente si está configurado #}
    {% if session.get('auth') %}
        
        <h1 style="margin-top: 40px;">Panel de Ejercicios</h1>
        <div class="container">
            {% for i in range(1, 4) %}
            <div class="card">
                <img src="https://picsum.photos/seed/{{i}}/300/200">
                <div class="card-body">
                    <h3>Ejercicio {{ i }}</h3>
                    <p>Descripción del ejercicio.</p>
                    <a href="#" class="btn">Ver Ejercicio</a>
                </div>
            </div>
            {% endfor %}
        </div>
        <a href="/logout" style="color: #ef4444; margin-bottom: 50px; text-decoration: none; font-weight: bold;">Cerrar Sesión</a>

    {% else %}

        <div class="login-card">
            <h2>Bienvenido</h2>
            <form method="POST" action="/login">
                <input type="text" name="usuario" placeholder="Usuario" required>
                <input type="password" name="password" placeholder="Contraseña" required>
                <button type="submit" class="btn" style="width: 100%;">Entrar</button>
            </form>
            {% if error %}<p style="color: red; font-size: 14px;">{{ error }}</p>{% endif %}
        </div>

    {% endif %}

</body>
</html>
"""

# --- RUTAS CONTROLADORAS ---

@app.route("/")
def index():
    # Solo mostramos la base, Jinja se encarga del resto con session
    return render_template_string(HTML_BASE)

@app.route("/login", methods=["POST"])
def login():
    u = request.form.get("usuario")
    p = request.form.get("password")
    
    if auth_manager.verificar(u, p):
        session['auth'] = True
        return redirect(url_for('index'))
    
    return render_template_string(HTML_BASE, error="Datos incorrectos")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)