import mysql.connector

# Conectar a la base de datos MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="tu_usuario",
    password="tu_contraseña",
    database="tu_base_de_datos"
)

cursor = conn.cursor()

# Llamar al procedimiento almacenado
nombre_usuario = "Benjamín Steck"
edad_usuario = 22

cursor.callproc('InsertarUsuario', [nombre_usuario, edad_usuario])

# Confirmar los cambios
conn.commit()

# Cerrar la conexión
cursor.close()
conn.close()