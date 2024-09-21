from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Crear la base de datos en memoria
engine = create_engine('sqlite:///:memory:', echo=True)

# Definir la base de la clase
Base = declarative_base()

# Definir la clase Usuario
class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    edad = Column(Integer)

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Crear la tabla
Base.metadata.create_all(engine)

# Crear una sesión para interactuar con la base de datos
Session = sessionmaker(bind=engine)
session = Session()

# Crear un nuevo usuario
nuevo_usuario = Usuario("Benjamín Steck", 22)

# Añadir el usuario a la sesión
session.add(nuevo_usuario)

# Guardar (commit) los cambios en la base de datos
session.commit()

# Consultar todos los usuarios
usuarios = session.query(Usuario).all()
for usuario in usuarios:
    print(f"ID: {usuario.id}, Nombre: {usuario.nombre}, Edad: {usuario.edad}")
