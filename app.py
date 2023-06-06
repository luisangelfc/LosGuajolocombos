from flask import Flask, redirect, url_for, render_template, request, session
from alchemyClasses.db import db, ReporteVentas
from SQL.credentials import username, passw
from controllers.controller_productos import productosBlueprint, get_products, agregar_producto, modificar_producto
from controllers.controller_itinerarios import itinerariosBlueprint, obtener_itinerarios
from controllers.controller_nuevo_cliente import registro_bp
from controllers.controller_info_cuenta import info_bp
from models.model_cliente import ADMIN, VENDEDOR, CLIENTE
from controllers.controller_inicio import inicio_bp
from controllers.controller_ordenes import ordenesBlueprint
from controllers.controller_sales_report import salesBlueprint
from controllers.controller_cliente_monitorea_pedido import customerOrdersBlueprint

from sqlalchemy import func

app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(registro_bp)
app.register_blueprint(inicio_bp)
app.register_blueprint(info_bp)
app.register_blueprint(productosBlueprint)
app.register_blueprint(itinerariosBlueprint)
app.register_blueprint(ordenesBlueprint)
app.register_blueprint(customerOrdersBlueprint)
app.register_blueprint(salesBlueprint)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://' + username + ':' + passw + '@localhost:5432/Ingenieria'

app.config.from_mapping(
    SECRET_KEY='dev'
)
db.init_app(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    return redirect(url_for('inicio.inicio'))


@app.route('/productos')
def product():
    return render_template('ProductosAdmin.html', productos=get_products())


@app.route('/obtainProductInfo', methods=['POST'])
def obtain_product_info():
    if request.method == 'POST' and session.get('usuario') is not None and session.get('credencial') == ADMIN:
        if "id_producto" not in request.form:
            print("NONE")
            return render_template('obtainProductInfo.html', id_prd = -1)
        else:
            return render_template('obtainProductInfo.html', id_prd=request.form['id_producto'])
    else:
        return render_template('inicio.html')


@app.route('/itinerarios')
def itinerario():
    if session['credencial'] is not None and session['credencial'] == ADMIN:
        return render_template('ItinerariosAdmin.html', itinerarios=obtener_itinerarios())
    else:
        return render_template('inicio.html')


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
