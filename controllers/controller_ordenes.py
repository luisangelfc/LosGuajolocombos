import datetime
from flask import Blueprint, render_template, request, redirect, url_for, session
from alchemyClasses.db import db, Orden, ReporteVentas
from models.model_cliente import ADMIN, VENDEDOR, CLIENTE
from datetime import datetime

ordenesBlueprint = Blueprint('ordenes', __name__, url_prefix='/ordenes')

@ordenesBlueprint.route('/')
def make_order():
    if session.get('credencial') is not None and session.get('credencial') == CLIENTE:
        return render_template('crear_orden.html')
    else:
        return redirect(url_for('info.info'))

@ordenesBlueprint.route('/crear', methods=['GET', 'POST'])
def create_order():
    if request.method == 'POST' and session.get('credencial') is not None and session.get('credencial') == CLIENTE:
        # Get form data
        id_usuario = int(request.form['id_usuario'])
        estatus = "Sin status"  # Assuming the initial status is "order placed"
        fecha = request.form['fecha']
        total = float(request.form['total'])

        # Create a new order instance
        new_order = Orden(id_usuario=id_usuario, estatus=estatus, fecha=fecha, total=total)

        # Save the new order to the database
        db.session.add(new_order)
        db.session.commit()

        # Redirect to the order detail page
        return render_template('cliente_monitorea_estatus.html', order=new_order)
        #return redirect(url_for('ordenes.view_order', order_id=new_order.id_orden))
    else:
        # Render the order creation form
        return redirect(url_for('info.info'))


@ordenesBlueprint.route('/<int:order_id>', methods=['GET', 'POST'])
def view_order(order_id):
    # Retrieve the order from the database
    order = Orden.query.get_or_404(order_id)

    if request.method == 'POST':
        # Get the new status from the form
        new_status = request.form['estatus']

        if new_status == 'orden entregada':
            # Create a new sales report
            report = ReporteVentas(
                fecha_inicio=order.fecha,
                fecha_fin=datetime.now().date(),
                total=order.total
            )
            db.session.add(report)
            db.session.commit()

            # Delete the order from the database
            #db.session.delete(order)
            #db.session.commit()

            # Redirect to the seller_view_orders page
            return redirect(url_for('ordenes.customer_orders'))

        # Update the order's status
        order.estatus = new_status
        db.session.commit()

        # Redirect back to the order detail page
        return redirect(url_for('ordenes.view_order', order_id=order.id_orden))

    # Render the order detail page
    return render_template('cambiar_estatus.html', order=order)


@ordenesBlueprint.route('/ver_ordenes')
def customer_orders():
    if session.get('credencial') is not None and session.get('credencial') == VENDEDOR:
        # Retrieve all orders from the database
        orders = Orden.query.all()

        # Render the orders list page
        return render_template('vendedor_ver_ordenes.html', orders=orders)

    elif session.get('credencial') is None:
        return render_template('inicio_sesión.html')
    else:
        redirect(url_for('info.info'))
