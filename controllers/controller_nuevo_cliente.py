import functools

from models.model_cliente import nombreExistente, contraseniaSegura, registraCliente

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for

registro_bp = Blueprint('registro', __name__, url_prefix = '/registro')

@registro_bp.route('/', methods = ['GET', 'POST'])
def registro():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasenia = request.form['contrasenia']
        if nombreExistente(usuario):
            return 'Nombre de usuario en uso'
        if not contraseniaSegura(contrasenia):
            return 'La contraseña es insegura'
        registraCliente(usuario, contrasenia)
        return redirect(url_for('registro.success')) # Esto debe llevar a la página de inicio
    else:
        return render_template('registro.html')

@registro_bp.route('/success', methods = ['GET'])
def success():
    return render_template('placeholder_inicio.html') # Cuando haya un menú de inicio hay que redirigir a ese.