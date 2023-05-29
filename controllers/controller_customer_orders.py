from flask import Blueprint, render_template
from alchemyClasses.db import Orden

customerOrdersBlueprint = Blueprint('customer_orders', __name__, url_prefix='/orders')


@customerOrdersBlueprint.route('/<int:order_id>')
def view_customer_order(order_id):
    # Retrieve the order from the database
    order = Orden.query.get_or_404(order_id)

    # Render the order detail page
    return render_template('customer_order.html', order=order)
