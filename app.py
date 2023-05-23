from flask import Flask, redirect, url_for
from alchemyClasses.db import db
from SQL.credentials import username,passw
from controllers.productos import productosBlueprint

from controllers.controller_nuevo_cliente import registro_bp
from controllers.controller_info_cuenta import info_bp



app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(registro_bp)
app.register_blueprint(info_bp)
app.register_blueprint(productosBlueprint)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://' + username + ':' + passw + '@localhost:5432/ingenieria'


app.config.from_mapping(
    SECRET_KEY = 'dev'
)
db.init_app(app)


@app.route('/', methods = ['GET', 'POST'])
def index():
    return redirect(url_for('registro.registro'))

if __name__ == '__main__':
    app.run(host = "localhost", port = 8000, debug = True)

