import datetime
from operator import and_
from flask import Blueprint, render_template
from alchemyClasses.db import ReporteVentas
from datetime import datetime, timedelta

salesBlueprint = Blueprint('sales', __name__, url_prefix='/sales')


@salesBlueprint.route('/')
def sales_reports():
    today = datetime.now().date()

    start_date_day = today
    end_date_day = today + timedelta(days=1)
    start_date_week = today - timedelta(days=7)
    end_date_week = today + timedelta(days=1)

    reports_day = ReporteVentas.query.filter(and_(ReporteVentas.fecha_inicio >= start_date_day, ReporteVentas.fecha_fin < end_date_day)).all()
    reports_week = ReporteVentas.query.filter(and_(ReporteVentas.fecha_inicio >= start_date_week, ReporteVentas.fecha_fin < end_date_week)).all()

    no_sales_message_day = "No hay ventas el día de hoy."
    no_sales_message_week = "No hay ventas en la semana."

    if not reports_day:
        no_sales_message_day = "No hay ventas el día de hoy."

    if not reports_week:
        no_sales_message_week = "No hay ventas en la semana."

    return render_template('sales_report.html', reports_day=reports_day, reports_week=reports_week, no_sales_message_day=no_sales_message_day, no_sales_message_week=no_sales_message_week)