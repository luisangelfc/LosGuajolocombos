from alchemyClasses.db import Producto, db


def find_product_by_name(product_name):
    return Producto.query.filter(Producto.nombre == product_name).first()


def get_product(id_product):
    return Producto.query.filter(Producto.id_producto == id_product).first()


def get_products():
    productos = Producto.query.all()
    return productos


def register_product(nombre, descripcion, precio, disponible, id_categoria):
    new_product = Producto(nombre, descripcion, precio, disponible, id_categoria)
    db.session.add(new_product)
    db.session.commit()


def modify_product(id_product, nombre, descripcion, precio, disponible, id_categoria):
    producto = get_product(id_product)
    producto.nombre = nombre
    producto.descripcion = descripcion
    producto.precio = precio
    producto.disponible = disponible
    producto.id_categoria_producto = id_categoria
    db.session.commit()


def delete_product(id_producto):
    producto = get_product(id_producto)
    db.session.delete(producto)
    db.session.commit()
