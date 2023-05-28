from flask import Flask, redirect, url_for, render_template, request
from alchemyClasses.db import db, ReporteVentas
from SQL.credentials import username, passw
from controllers.controller_productos import productosBlueprint, get_products, agregar_producto, modificar_producto
from controllers.controller_itinerarios import itinerariosBlueprint, obtener_itinerarios
from controllers.controller_nuevo_cliente import registro_bp
from controllers.controller_info_cuenta import info_bp
from datetime import datetime, timedelta
from sqlalchemy import and_

app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(registro_bp)
app.register_blueprint(info_bp)
app.register_blueprint(productosBlueprint)
app.register_blueprint(itinerariosBlueprint)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://' + username + ':' + passw + '@localhost:5432/guajolocombos'

app.config.from_mapping(
    SECRET_KEY='dev'
)
db.init_app(app)

def create_tables():
    with app.app_context():
        db.create_all()

create_tables()


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
    if request.method == 'POST':
        print(request.form)
        if request.form.__len__() != 1:
            return render_template('obtainProductInfo.html')
        else:
            return render_template('obtainProductInfo.html', id_prd = request.form['id_producto'])


@app.route('/itinerarios')
def itinerario():
    return render_template('ItinerariosAdmin.html', itinerarios=obtener_itinerarios())


@app.route('/sales_reports', methods=['GET'])
def sales_reports():
    today = datetime.now().date()

    start_date_day = today
    end_date_day = today + timedelta(days=1)
    start_date_week = today - timedelta(days=7) 
    end_date_week = today

    reports_day = ReporteVentas.query.filter(and_(ReporteVentas.fecha_inicio >= start_date_day, ReporteVentas.fecha_fin < end_date_day)).all()
    reports_week = ReporteVentas.query.filter(and_(ReporteVentas.fecha_inicio >= start_date_week, ReporteVentas.fecha_fin < end_date_week)).all()

    no_sales_message = "No hay ventas el día de hoy."

    if not reports_day:
        no_sales_message = "No hay ventas el día de hoy."

    return render_template('sales_report.html', reports_day=reports_day, reports_week=reports_week, no_sales_message=no_sales_message)


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
