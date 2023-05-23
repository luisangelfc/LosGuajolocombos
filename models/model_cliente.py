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

def bajaCliente(nombre):
    user = Usuario.query.filter(Usuario.nombre == nombre).first()
    db.session.delete(user)
    db.session.commit()

def actualizaNombreCliente(antiguo, nuevo):
    user = Usuario.query.filter(Usuario.nombre == antiguo).first()
    user.nombre = nuevo
    db.session.commit()

def actualizaContrasenia(usuario, nueva_contra):
    user = Usuario.query.filter(Usuario.nombre == usuario).first()
    user.contrasenia = nueva_contra
    db.session.commit()

def getDireccion(usuario):
    user = Usuario.query.filter(Usuario.nombre == usuario).first()
    return user.direccion

def actualizaDireccion(usuario, direccion):
    user = Usuario.query.filter(Usuario.nombre == usuario).first()
    user.direccion = direccion
    db.session.commit()

def verificaContrasenia(usuario, contrasenia):
    user = Usuario.query.filter(Usuario.nombre == usuario, Usuario.contrasenia == contrasenia).first()
    return user != None