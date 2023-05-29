from flask import Blueprint, render_template, request, redirect, url_for
from alchemyClasses.db import db, Orden

ordenesBlueprint = Blueprint('ordenes', __name__, url_prefix='/ordenes')


@ordenesBlueprint.route('/create', methods=['GET', 'POST'])
def create_order():
    if request.method == 'POST':
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
        return redirect(url_for('ordenes.view_order', order_id=new_order.id_orden))

    # Render the order creation form
    return render_template('crear_orden.html')


@ordenesBlueprint.route('/<int:order_id>', methods=['GET', 'POST'])
def view_order(order_id):
    # Retrieve the order from the database
    order = Orden.query.get_or_404(order_id)

    if request.method == 'POST':
        # Get the new status from the form
        new_status = request.form['estatus']
        
        # Update the order's status
        order.estatus = new_status
        db.session.commit()

        # Redirect back to the order detail page
        return redirect(url_for('ordenes.view_order', order_id=order.id_orden))

    # Render the order detail page
    return render_template('ver_orden.html', order=order)
