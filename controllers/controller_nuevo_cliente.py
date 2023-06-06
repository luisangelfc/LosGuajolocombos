from models.model_cliente import nombreExistente, contraseniaSegura, registraCliente, getCliente, getCredencial, getClienteId

from flask import Blueprint, flash, redirect, render_template, request, session, url_for

registro_bp = Blueprint('registro', __name__, url_prefix = '/registro')

@registro_bp.route('/', methods = ['GET', 'POST'])
def registro():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasenia = request.form['contrasenia']
        if nombreExistente(usuario):
            flash('Nombre de usuario en uso')
            return redirect(url_for('registro.registro'))
        if not contraseniaSegura(contrasenia):
            flash('La contraseña es insegura')
            return redirect(url_for('registro.registro'))
        registraCliente(usuario, contrasenia)
        session.clear()
        cliente = getCliente(usuario)
        session['usuario'] = cliente.id_usuario
        session['credencial'] = getCredencial(usuario)
        return redirect(url_for('registro.success'))
    else:
        return render_template('registro.html')

@registro_bp.route('/success', methods = ['GET'])
def success():
    if session.get('usuario') != None:
        cliente = getClienteId(session.get('usuario'))
        return render_template('info.html', cliente = cliente)
    flash("Error: no se ha iniciado sesión")
    return redirect(url_for('registro.registro'))