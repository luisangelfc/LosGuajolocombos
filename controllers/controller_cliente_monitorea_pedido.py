from flask import Blueprint, render_template, redirect, url_for
from alchemyClasses.db import Orden

customerOrdersBlueprint = Blueprint('customer_orders', __name__, url_prefix='/orden')


@customerOrdersBlueprint.route('/<int:order_id>')
def view_customer_order(order_id):
    # Retrieve the order from the database
    order = Orden.query.get(order_id)

    # Check if the order exists
    if order is None:
        # Redirect to a page indicating the order has been delivered
        return redirect(url_for('customer_orders.order_delivered'))

    # Render the order detail page
    return render_template('cliente_monitorea_estatus.html', order=order)


@customerOrdersBlueprint.route('orden_entregada')
def order_delivered():
    return render_template('orden_entregada.html')
