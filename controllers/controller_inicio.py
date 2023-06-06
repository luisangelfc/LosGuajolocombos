from models.model_cliente import nombreExistente, verificaContrasenia, getCliente, getCredencial

from flask import Blueprint, flash, redirect, render_template, request, session, url_for

inicio_bp = Blueprint('inicio', __name__, url_prefix = '/inicio')

@inicio_bp.route('/', methods = ['GET', 'POST'])
def inicio():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasenia = request.form['contrasenia']
        if not nombreExistente(usuario):
            flash('Nombre de usuario no encontrado')
            return redirect(url_for('inicio.inicio'))
        if not verificaContrasenia(usuario, contrasenia):
            flash('Contraseña incorrecta')
            return redirect(url_for('inicio.inicio'))
        cliente = getCliente(usuario)
        session['usuario'] = cliente.id_usuario
        session['credencial'] = getCredencial(cliente.nombre)
        return render_template('info.html', cliente = cliente)
    else:
        return render_template('inicio_sesión.html')