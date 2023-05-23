from alchemyClasses.db import Producto


def find_product_by_name(product_name):
    return Producto.query.filter(Producto.nombre == product_name)


def get_product(id_product):
    return Producto.query.filter(Producto.id_producto == id_product).first()


def get_products():
    return Producto.query.all()

def register_product(producto):

