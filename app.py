from alchemyClasses.db import db
from controllers.controller_nuevo_cliente import registro_bp
from controllers.controller_info_cuenta import info_bp

from flask import Flask, redirect, url_for

app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(registro_bp)
app.register_blueprint(info_bp)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://guajolocombos:tortadetamal@localhost:5432/guajolocombos'
app.config.from_mapping(
    SECRET_KEY = 'dev'
)
db.init_app(app)

@app.route('/', methods = ['GET', 'POST'])
def index():
    return redirect(url_for('registro.registro'))

if __name__ == '__main__':
    app.run(host = "localhost", port = 8000, debug = True)