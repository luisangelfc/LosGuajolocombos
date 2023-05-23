from models.model_cliente import nombreExistente, bajaCliente, actualizaNombreCliente, actualizaContrasenia, \
    contraseniaSegura, getDireccion, actualizaDireccion, verificaContrasenia

from flask import Blueprint, flash, redirect, render_template, request, session, url_for

info_bp = Blueprint('info', __name__, url_prefix='/info')


@info_bp.route('/', methods=['GET'])
def info():
    if session.get('usuario') is not None:
        direccion = getDireccion(session.get('usuario'))
        return render_template('info.html', direccion=direccion)
    flash("Error: no se ha iniciado sesión")
    return redirect(url_for('registro.registro'))  # Debe cambiarse por el de iniciar sesión


@info_bp.route('/user_change', methods=['GET', 'POST'])
def user_change():
    if session.get('usuario') is None:
        flash("Error: no se ha iniciado sesión")
        return redirect(url_for('registro.registro'))  # Debe cambiarse por el de iniciar sesión
    if request.method == 'POST':
        nuevo_usuario = request.form['nuevo_nombre']
        if nombreExistente(nuevo_usuario):
            flash('Nombre de usuario en uso')
            return redirect(url_for('info.user_change'))

        actualizaNombreCliente(session.get('usuario'), nuevo_usuario)
        session['usuario'] = nuevo_usuario
        flash('Nombre cambiado con éxito')
        return redirect(url_for('info.info'))
    else:
        return render_template('cambiar_nombre.html')


@info_bp.route('/password_change', methods=['GET', 'POST'])
def password_change():
    if session.get('usuario') is None:
        flash("Error: no se ha iniciado sesión")
        return redirect(url_for('registro.registro'))  # Debe cambiarse por el de iniciar sesión
    if request.method == 'POST':
        nueva_contra = request.form['nueva_contra']
        if nueva_contra == session.get('contrasenia'):
            flash('La contraseña no tiene cambios')
            return redirect(url_for('info.password_change'))
        if not contraseniaSegura(nueva_contra):
            flash('La contraseña es insegura')
            return redirect(url_for('info.password_change'))
        actualizaContrasenia(session.get('usuario'), nueva_contra)
        session['contrasenia'] = nueva_contra
        flash('Contraseña cambiada con éxito')
        return redirect(url_for('info.info'))
    else:
        return render_template('cambiar_contraseña.html')


@info_bp.route('/dir_change', methods=['GET', 'POST'])
def dir_change():
    if session.get('usuario') is None:
        flash("Error: no se ha iniciado sesión")
        return redirect(url_for('registro.registro'))  # Debe cambiarse por el de iniciar sesión
    if request.method == 'POST':
        direccion = request.form['direccion']
        actualizaDireccion(session.get('usuario'), direccion)
        flash('Direccion cambiada con éxito')
        return redirect(url_for('info.info'))
    else:
        return render_template('cambiar_direccion.html')


@info_bp.route('/delete_user', methods=['GET', 'POST'])
def delete_user():
    if session.get('usuario') is None:
        flash("Error: no se ha iniciado sesión")
        return redirect(url_for('registro.registro'))  # Debe cambiarse por el de iniciar sesión
    if request.method == 'POST':
        contrasenia = request.form['contrasenia']
        if not verificaContrasenia(session.get('usuario'), contrasenia):
            flash('Contraseña incorrecta')
            return redirect(url_for('info.delete_user'))
        bajaCliente(session.get('usuario'))
        session.clear()
        flash('Cuenta eliminada exitosamente')
        return redirect(url_for('registro.registro'))  # Debe cambiarse por el de iniciar sesión o algún otro
    else:
        return render_template('eliminar_cuenta.html')
