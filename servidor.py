from flask import Flask, request, jsonify
import bdd

app = Flask(__name__)

@app.route('/registro', methods=['POST'])
def ruta_registro():
    datos = request.get_json()
    exito = bdd.registrar_usuario(datos.get('usuario'), datos.get('contraseña'))

    if exito:
        return jsonify({"mensaje": "Usuario creado"}), 201
    return jsonify({"error": "No se pudo crear el usuario"}), 400

@app.route('/login', methods=['POST'])
def ruta_login():
    datos = request.get_json()
    if bdd.verificar_credenciales(datos.get('usuario'), datos.get('contraseña')):
        return jsonify({"mensaje": "Acceso permitido", "auth": True}), 200
    return jsonify({"error": "Usuario o contraseña incorrectos"}), 401

@app.route('/tareas', methods=['GET'])
def mostrar_bienvenida():
    """Endpoint que devuelve un HTML de bienvenida simple."""
    return """
        <html>
            <body style="font-family: sans-serif; background-color: #f0f0f0;">
                <h2>Panel de Gestión de Tareas</h2>
                <p>Hola. Has ingresado correctamente.</p>
                <hr>
                <ul>
                    <li>1. Ver mis tareas pendientes</li>
                    <li>2. Agregar nueva tarea</li>
                    <li>3. Salir</li>
                </ul>
            </body>
        </html>
    """, 200

if __name__ == '__main__':
    print("Inicializando componentes del sistema...")
    if bdd.inicializar_bdd():
        print("Base de datos conectada")
        app.run(debug=True, port=5000)
    else: 
        print("Error crítico. No se pudo iniciar el sistema de datos.")