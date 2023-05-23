from flask import Flask, redirect, url_for, render_template, request
from alchemyClasses.db import db
from SQL.credentials import username, passw
from controllers.controller_productos import productosBlueprint, get_products, agregar_producto, modificar_producto
from controllers.controller_itinerarios import itinerariosBlueprint, obtener_itinerarios
from controllers.controller_nuevo_cliente import registro_bp
from controllers.controller_info_cuenta import info_bp

app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(registro_bp)
app.register_blueprint(info_bp)
app.register_blueprint(productosBlueprint)
app.register_blueprint(itinerariosBlueprint)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://' + username + ':' + passw + '@localhost:5432/Ingenieria'

app.config.from_mapping(
    SECRET_KEY='dev'
)
db.init_app(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    return redirect(url_for('registro.registro'))


@app.route('/productos')
def product():
    products = get_products()
    for product in products:
        print(product.nombre)
    return render_template('ProductosAdmin.html', productos=products)


@app.route('/obtainProductInfo', methods=['POST'])
def obtain_product_info():
    if request.method == 'POST' :
        id_producto = request.form['id_producto']
        if id_producto is None :
            return render_template('obtainProductInfo.html')
        else:
            return render_template('obtainProductInfo.html', id_prd = id_producto)


@app.route('/itinerarios')
def itinerario():
    return render_template('ItinerariosAdmin.html', itinerarios=obtener_itinerarios())


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
