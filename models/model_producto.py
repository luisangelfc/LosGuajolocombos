from alchemyClasses.db import Producto


def get_product(id_product):
    return Producto.query.filter(Producto.id_producto == id_product).first()


def get_products():
    return Producto.query.all()
