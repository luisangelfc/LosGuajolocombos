from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for

productosBlueprint = Blueprint('productos', __name__, url_prefix='/productos')
@productosBlueprint.route('/', methods=["GET", "POST"])
def productos()