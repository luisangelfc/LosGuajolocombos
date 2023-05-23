from alchemyClasses.db import Producto, CategoriaProducto


def find_categoria_producto_by_name(name):
    return CategoriaProducto.query.filter(CategoriaProducto.nombre == name)
