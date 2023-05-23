from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
from alchemyClasses.db import Producto
from models.model_producto import get_products, get_product, find_product_by_name

productosBlueprint = Blueprint('productos', __name__, url_prefix='/productos')


@productosBlueprint.route('/productos', methods=["GET"])
def obtener_productos():
    if request.method == 'GET':
        return jsonify(get_products())

@productosBlueprint.route('/addProduct', methods=["POST"])
def agregar_productos():
    if request.method == 'POST':
        producto = request.json
        if find_product_by_name(producto['nombre']) is None:
            producto = Producto(
                producto['']
            )
