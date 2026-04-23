// --- 1. Variables Globales (Para que todas las funciones las vean) ---
let html5QrCode;
const config = { fps: 10, qrbox: { width: 250, height: 150 } };

// --- 2. Cuando la página cargue, iniciamos todo ---
window.addEventListener('load', function () {
    html5QrCode = new Html5Qrcode("reader");

    iniciarEscaneo();
});

// --- 3. Funciones de control ---
function iniciarEscaneo() {
    html5QrCode.start(
        { facingMode: "environment" },
        config,
        (decodedText) => {
            console.log(`Código detectado: ${decodedText}`);
            // Paramos el escáner al detectar para evitar escaneos múltiples
            html5QrCode.stop().then(() => {
                consultarProducto(decodedText);
            });
        },
        (errorMessage) => { /* ignorar errores de lectura constante */ }
    ).catch(err => {
        console.error("No se pudo iniciar la cámara: ", err);
    });
}

async function consultarProducto(codigo) {
    try {
        const response = await fetch(`/api/producto/${codigo}`);
        const data = await response.json();

        if (response.ok) {
            document.getElementById('nombre-prod').innerText = data.nombre;
            document.getElementById('precio-prod').innerText = data.precio;
            document.getElementById('resultado').style.display = 'block';
            
            // Si el producto existía, reiniciamos el escaneo tras unos segundos
            setTimeout(() => {
                document.getElementById('resultado').style.display = 'none';
                iniciarEscaneo();
            }, 3000);
        } else {
            // Producto no existe, mostramos formulario
            document.getElementById('form-registro').style.display = 'block';
            document.getElementById('nuevo-codigo').innerText = codigo;
        }
    } catch (error) {
        console.error("Error consultando:", error);
    }
}

async function guardarProducto() {
    const codigo = document.getElementById('nuevo-codigo').innerText;
    const nombre = document.getElementById('nombre-input').value;
    const precio = document.getElementById('precio-input').value;

    if (!nombre || !precio) {
        alert("Llena todo, porfa");
        return;
    }

    try {
        const response = await fetch('/api/producto/registrar', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ codigo, nombre, precio: parseFloat(precio) })
        });

        if (response.ok) {
            alert("Producto guardado");
            document.getElementById('form-registro').style.display = 'none';
            document.getElementById('nombre-input').value = '';
            document.getElementById('precio-input').value = '';
            
            // Reiniciamos el ciclo
            iniciarEscaneo();
        }
    } catch (error) {
        console.error("Error al guardar:", error);
    }
}