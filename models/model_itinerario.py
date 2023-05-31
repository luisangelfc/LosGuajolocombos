from alchemyClasses.db import Itinerario, db

def get_itinerarios():
    return Itinerario.query.all()