from flask import Flask
from controllers.productos import productosBlueprint
from SQL.credentials import username,passw
from alchemyClasses.db import db

app = Flask(__name__)
app.register_blueprint(productosBlueprint)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://' + username + ':' + passw + '@localhost:5432/ingenieria'
app.config.from_mapping(
    SECRET_KEY = 'dev'
)
db.init_app(app)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
