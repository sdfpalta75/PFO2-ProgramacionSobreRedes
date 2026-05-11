import requests
import webbrowser

URL_BASE = 'http://127.0.0.1:5000'

def mostrar_menu_principal():
    print("\n--- SISTEMA DE GESTION DE TAREAS ---")
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Salir")
    return input("Ingrese una opción: ")

def ejecutar_registro():
    usuario = input("Ingrese nombre de usuario: ")
    clave = input("Ingrese contraseña: ")

    payload = {"usuario": usuario, "contraseña": clave}

    try:
        respuesta = requests.post(f"{URL_BASE}/registro", json=payload)

        if respuesta.status_code == 201:
            print(f"Exito: {respuesta.json().get('mensaje')}")
        else: 
            print(f"Error: {respuesta.json().get('error')}")
    except requests.exceptions.ConnectionError:
        print("Error: No se pudo conectar con el servidor.")

def ejecutar_login():
    usuario = input("Ingrese nombre de usuario: ")
    clave = input("Ingrese contraseña: ")

    payload = {"usuario": usuario, "contraseña": clave}

    try:
        respuesta = requests.post(f"{URL_BASE}/login", json=payload)

        if respuesta.status_code == 200:
            print(f"\n>>> {respuesta.json().get('mensaje')} <<<")
            print("Abriendo panel de tareas en el navegador...")
            webbrowser.open(f"{URL_BASE}/tareas")
            acceder_a_tareas()
        else:
            print(f"Error: {respuesta.json().get('error')}")
    except requests.exceptions.ConnectionError:
        print("Error: No se pudo conectar con el servidor.")

def acceder_a_tareas():
    try:
        respuesta = requests.get(f"{URL_BASE}/tareas")

        if respuesta.status_code == 200:
            print("\n--- CONTENIDO DE LA RURA /TAREAS ---")
            print(respuesta.text)
            print("------------------------------------")
            input("Presione Enter para volver al menú principal...")
    except Exception as e:
        print(f"No se pudo cargar el panel de tareas. Error: {e}")

if __name__ == '__main__':
    while True:
        opcion = mostrar_menu_principal()

        if opcion == '1':
            ejecutar_registro()
        elif opcion == '2':
            ejecutar_login()
        elif opcion == '3':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción incorrecta.")
