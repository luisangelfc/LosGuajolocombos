from flask import Blueprint, flash, render_template, request
from sqlalchemy import true, false

from models.model_categoria_producto import find_categoria_producto_by_name, find_categoria_by_id
from models.model_producto import get_products, get_product, find_product_by_name, register_product, modify_product, \
    delete_product

productosBlueprint = Blueprint('productos', __name__, url_prefix='/productos')


@productosBlueprint.route('/', methods=["GET"])
def obtener_productos():
    if request.method == 'GET':
        return get_products()


@productosBlueprint.route('/', methods=["POST"])
def agregar_producto():
    if request.method == 'POST':
        producto = request.form
        if find_product_by_name(producto['nombre']) is None:
            categoria = find_categoria_by_id(producto['id_categoria_producto'])
            if categoria is not None:
                if producto['disponible'] == 'True':
                    disp = True
                else:
                    disp = False
                register_product(producto['nombre'], producto['descripcion'], producto['precio'], disp,
                                 producto['id_categoria_producto'])
                flash('Registro Exitoso')
            else:
                flash('La categoria seleccionada no existe')
        else:
            flash('Ya existe un producto con ese nombre')
        return render_template('ProductosAdmin.html', productos = get_products())


@productosBlueprint.route('/modProduct', methods=["POST"])
def modificar_producto():
    if request.method == 'POST':
        producto = request.form
        print(request.form)
        categoria = find_categoria_by_id(producto['id_categoria_producto'])
        print(producto['id_producto'])
        if get_product(producto['id_producto']) is not None:
            print('pass')
            if categoria is not None:
                if producto['disponible'] == 'True':
                    disp = True
                else:
                    disp = False

                modify_product(producto['id_producto'],producto['nombre'], producto['descripcion'], producto['precio'], disp,
                               producto['id_categoria_producto'])
                flash('Modificacion Exitosa')
            else:
                flash('La categoria seleccionada no existe')
        else:
            flash('no existe ese producto')
        return render_template('ProductosAdmin.html', productos = get_products())


@productosBlueprint.route('/delProduct', methods=["POST"])
def borrar_producto():
    if request.method == 'POST':
        product_received = request.form
        product = get_product(product_received['id_producto'])
        if product is not None:
            delete_product(product_received['id_producto'])
            flash('Borrado Exitoso')
        else:
            flash('no existe ese producto')
        return render_template('ProductosAdmin.html', productos = get_products())

