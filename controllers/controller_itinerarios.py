from flask import Blueprint, flash, render_template, request

from models.model_itinerario import get_itinerarios

itinerariosBlueprint = Blueprint('itinerarios', __name__, url_prefix='/itinerario')


@itinerariosBlueprint.route('/itinerarios', methods=["GET"])
def obtener_itinerarios():
    if request.method == 'GET':
        return get_itinerarios()
