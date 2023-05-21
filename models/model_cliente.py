import re
from alchemyClasses.db import Usuario, db

def nombreExistente(nombre):
    return Usuario.query.filter(Usuario.nombre == nombre).first() != None

def contraseniaSegura(contrasenia):
    return len(contrasenia) >= 8 and re.search(r'[a-z]', contrasenia) != None and re.search(r'[A-Z]', contrasenia) != None and re.search(r'[0-9]', contrasenia) != None

def registraCliente(nombre, contrasenia):
    nuevo_cliente = Usuario(nombre, contrasenia)
    db.session.add(nuevo_cliente)
    db.session.commit()