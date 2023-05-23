from alchemyClasses.db import Producto, CategoriaProducto, db


def find_categoria_producto_by_name(name):
    return CategoriaProducto.query.filter(CategoriaProducto.nombre == name).first()


def find_categoria_by_id(id):
    return CategoriaProducto.query.filter(CategoriaProducto.id_categoria_producto == id).first()
