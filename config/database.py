import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#Se guardará el nombre de la base de datos
sqlite_file_name = "../database.sqlite"
#Se leerá el directorio actual del archivo database
base_dir = os.path.dirname(os.path.realpath(__file__))

#sqlite:/// es la forma en la que se conecta a una base de datos,
# se usa el método join para unir las urls

database_url = f"sqlite:///{os.path.join(base_dir,sqlite_file_name)}"

#esta es una variable que sirve como motor de la base de datos
engine = create_engine(database_url, echo=True)
#echo sirve para que nos muestre por consola lo que está pasando
#variable para crear sesión y conectarse a la base de datos
Session = sessionmaker(bind=engine)
#Sirve para manipular todas las tablas de la base de datos
Base = declarative_base() 