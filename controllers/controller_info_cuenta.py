from models.model_cliente import getClienteId, getCredencial, nombreExistente, bajaCliente, actualizaNombreCliente, actualizaContrasenia, \
    contraseniaSegura, actualizaDireccion, verificaContrasenia, ADMIN

from flask import Blueprint, flash, redirect, render_template, request, session, url_for

info_bp = Blueprint('info', __name__, url_prefix='/info')


@info_bp.route('/', methods=['GET'])
def info():
    if session.get('usuario') != None:
        cliente = getClienteId(session.get('usuario'))
        return render_template('info.html', cliente=cliente)
    flash("Error: no se ha iniciado sesión")
    return redirect(url_for('inicio.inicio'))


@info_bp.route('/user_change', methods=['GET', 'POST'])
def user_change():
    if session.get('usuario') == None:
        flash("Error: no se ha iniciado sesión")
        return redirect(url_for('inicio.inicio'))
    if request.method == 'POST':
        nuevo_usuario = request.form['nuevo_nombre']
        if nombreExistente(nuevo_usuario):
            flash('Nombre de usuario en uso')
            return redirect(url_for('info.user_change'))
        cliente = getClienteId(session.get('usuario'))
        actualizaNombreCliente(cliente.nombre, nuevo_usuario)
        flash('Nombre cambiado con éxito')
        return redirect(url_for('info.info'))
    else:
        return render_template('cambiar_nombre.html')


@info_bp.route('/password_change', methods=['GET', 'POST'])
def password_change():
    if session.get('usuario') == None:
        flash("Error: no se ha iniciado sesión")
        return redirect(url_for('inicio.inicio'))
    if request.method == 'POST':
        nueva_contra = request.form['nueva_contra']
        cliente = getClienteId(session.get('usuario'))
        if cliente.contrasenia == nueva_contra:
            flash('La contraseña no tiene cambios')
            return redirect(url_for('info.password_change'))
        if not contraseniaSegura(nueva_contra):
            flash('La contraseña es insegura')
            return redirect(url_for('info.password_change'))
        actualizaContrasenia(cliente.nombre, nueva_contra)
        flash('Contraseña cambiada con éxito')
        return redirect(url_for('info.info'))
    else:
        return render_template('cambiar_contraseña.html')


@info_bp.route('/dir_change', methods=['GET', 'POST'])
def dir_change():
    if session.get('usuario') == None:
        flash("Error: no se ha iniciado sesión")
        return redirect(url_for('registro.registro'))
    if session.get('credencial') == 1:
        return redirect(url_for('info.info'))
    if request.method == 'POST':
        direccion = request.form['direccion']
        cliente = getClienteId(session.get('usuario'))
        actualizaDireccion(cliente.nombre, direccion)
        flash('Direccion cambiada con éxito')
        return redirect(url_for('info.info'))
    else:
        return render_template('cambiar_direccion.html')


@info_bp.route('/delete_user', methods=['GET', 'POST'])
def delete_user():
    if session.get('usuario') == None:
        flash("Error: no se ha iniciado sesión")
        return redirect(url_for('inicio.inicio'))
    if session.get('credencial') != 2:
        return "No eres usuario"
    if request.method == 'POST':
        contrasenia = request.form['contrasenia']
        cliente = getClienteId(session.get('usuario'))
        if not verificaContrasenia(cliente.nombre, contrasenia):
            flash('Contraseña incorrecta')
            return redirect(url_for('info.delete_user'))
        bajaCliente(cliente.nombre)
        session.clear()
        flash('Cuenta eliminada exitosamente')
        return redirect(url_for('inicio.inicio'))
    else:
        return render_template('eliminar_cuenta.html')
