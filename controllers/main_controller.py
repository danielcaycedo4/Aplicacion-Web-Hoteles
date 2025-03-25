from flask import Blueprint, render_template, request
from models.ciudades_repository import get_all_ciudades
from models.hoteles_repository import get_hoteles_by_ciudad
from models.habitaciones_repository import get_habitaciones_by_hotel

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET'])
def index():
    ciudades = get_all_ciudades()
    ciudad_id = request.args.get('ciudad')
    hoteles = []
    habitaciones = {}

    if ciudad_id:
        hoteles = get_hoteles_by_ciudad(ciudad_id)
        for hotel in hoteles:
            habitaciones[hotel[0]] = get_habitaciones_by_hotel(hotel[0])

    return render_template('index.html', ciudades=ciudades, hoteles=hoteles, habitaciones=habitaciones)
