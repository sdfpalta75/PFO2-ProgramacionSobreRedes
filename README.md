# PFO2-ProgramacionSobreRedes

## Propuesta Formativa Obligatoria Nro 2, Programacion sobre Redes, IFTS29

### Link del proyecto: https://github.com/sdfpalta75/PFO2-ProgramacionSobreRedes.git

### Página: https://sdfpalta75.github.io/PFO2-ProgramacionSobreRedes/

### Pasos para correr la solución
1.- clonar el repositorio https://github.com/sdfpalta75/PFO2-ProgramacionSobreRedes.git
2.- No obligatorio, pero aconsejable, es crear un entorno virtual dentro de la carpeta de la solución
    mediante: python -m venv env (env es el nombre que se le da al entorno virtual)
    y activarlo mediante: windows ---> env\Scripts\activate
                          Linux/macOS ---> source env/bin/activate
                          (en ambos casos 'env' refiere al nombre dado al entorni virtual al crearlo)
3.- instalar las dependencias con el siguiente comando:
    pip install -r dependencias.txt
4.- En una terminal inicializar el servidor mediante "python servidor.py"
5.- Con el servidor abierto, en otra terminal ejecutar "python cliente.py"
6.- Desde el cliente podrá registrar un nuevo usuario o también loguearse uno ya existente.

El mensaje de bienvenida al que hace referencia la práctica, dado a que referencia a la ruta /tareas, no se tomó como un mensaje general del sistema, sino como un mensaje de bienvenida al panel de tareas, luego de un logueo exitoso.

### Respuestas conceptuales:
La práctica de hashear contraseñas es un método fundamental de seguridad, ya que si un atacante logra acceder a la base de datos del servidor, sólo verá un código extraño que nunca coincidirá con la contraseña real.

Las ventajas de usar SQLite en este proyecto son la persistencia de datos y la organización de los mismos, pero fundamentalmente, en este ámbito académico, lo es su ligereza, ya que el motor de la misma se halla integrado en python.

## Capturas de pantalla

### Registro de usuario exitoso
![Registro de usuario exitoso.](/capturas/Registro_exitoso.png)

### Logueo exitoso
![Logueo exitoso.](/capturas/Logueo_exitoso.png)



