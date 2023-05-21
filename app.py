from alchemyClasses.db import db
from controllers.controller_nuevo_cliente import registro_bp

from flask import Flask, redirect, url_for

app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(registro_bp)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://pppkizbroutle:14156362514v_R@localhost:5432/Guajolocombos'
db.init_app(app)

@app.route('/', methods = ['GET', 'POST'])
def index():
    return redirect(url_for('registro.registro'))

if __name__ == '__main__':
    app.run(host = "localhost", port = 8000, debug = True)