import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

NOMBRE_BDD = 'gestion_tareas.db'

def inicializar_bdd():
    """ Crea la tabla usuarios si no existe. """

    conexion = None
    try:
        conexion = sqlite3.connect(NOMBRE_BDD)
        cursor = conexion.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        conexion.commit()
        return True
    except sqlite3.Error as e:
        print(f"No se pudo inicializar la base de datos. Error: {e}")
        return False
    finally:
        # Cierre de la conexion a la bdd si fue abierta.
        if conexion:
            conexion.close()
    
def registrar_usuario(nombre, clave_plana):
    """ Guarda un nuevo usuario con contraseña hasheada. """

    conexion = None
    try:
        clave_hasheada = generate_password_hash(clave_plana)
        conexion = sqlite3.connect(NOMBRE_BDD)
        cursor = conexion.cursor()
        cursor.execute('''
            INSERT INTO usuarios (usuario, password)
            VALUES (?, ?)
        ''', (nombre, clave_hasheada))
        conexion.commit()
        return True
    except sqlite3.IntegrityError:
        print(f"El usuario '{nombre}' ya existe.")
        return False
    except sqlite3.Error as e:
        print(f"Error al registrar usuario: {e}")
        return False
    finally:
        if conexion:
            conexion.close()

def verificar_credenciales(nombre, clave_plana):
    """ Compara la clave ingresada con el hash guardado. """

    conexion = None
    try:
        conexion = sqlite3.connect(NOMBRE_BDD)
        cursor = conexion.cursor()
        cursor.execute("SELECT password FROM usuarios WHERE usuario = ?", (nombre,))
        resultado = cursor.fetchone()

        if resultado:
            clave_guardada = resultado[0]
            return check_password_hash(clave_guardada, clave_plana)
        return False
    except sqlite3.Error as e:
        print(f"Error al verificar credenciales: {e}")
        return False
    finally:
        if conexion:
            conexion.close()
            