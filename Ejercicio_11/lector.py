from flask import Flask, render_template_string

app = Flask(__name__)

# Aquí metemos todo el HTML y CSS en una sola variable
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Scanner perron roba datos</title>
    <script src="https://unpkg.com/html5-qrcode"></script>
    <style>
        body { 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
            text-align: center; 
            background: #1a1a1a; 
            color: #eee; 
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 500px;
            margin: auto;
            background: #2d2d2d;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.5);
        }
        #reader { 
            width: 100% !important; 
            border: none !important;
            border-radius: 10px;
            overflow: hidden;
        }
        .result-box { 
            margin-top: 20px;
            padding: 15px;
            background: #3d3d3d;
            border-left: 5px solid #00ff88;
            border-radius: 5px;
        }
        #result { 
            font-weight: bold; 
            color: #00ff88; 
            word-break: break-all;
        }
        button {
            background: #00ff88 !important;
            color: #1a1a1a !important;
            border: none !important;
            padding: 10px 20px !important;
            border-radius: 5px !important;
            cursor: pointer;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2> Escáner de Códigos</h2>
        <p>Apunta con la cámara de tu lap o cel perro</p>
        
        <div id="reader"></div>
        
        <div class="result-box">
            <span>Resultado:</span>
            <div id="result">Esperaa viejo..</div>
        </div>
    </div>

    <script>
        function onScanSuccess(decodedText, decodedResult) {
            // Ponemos el texto en el div de resultado
            document.getElementById('result').innerText = decodedText;
            
            // Si es un link, que se pueda picar
            if(decodedText.startsWith('http')) {
                document.getElementById('result').innerHTML = `<a href="${decodedText}" target="_blank" style="color: #00ff88;">${decodedText}</a>`;
            }

            // Un pitido o vibración (opcional)
            console.log(`Código: ${decodedText}`);
        }

        function onScanFailure(error) {
            // Errores de enfoque, no pasa nada
        }

        let html5QrcodeScanner = new Html5QrcodeScanner(
            "reader", { fps: 10, qrbox: {width: 250, height: 250} }, false);
        html5QrcodeScanner.render(onScanSuccess, onScanFailure);
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    # Mandamos el string de arriba como si fuera un archivo HTML
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    # host='0.0.0.0' para que ngrok y otros dispositivos te vean
    app.run(host='0.0.0.0', port=5000, debug=True)