from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

bp = Blueprint('index', __name__)

from ..crawler.crawler_utils import getWeather, getLocalCityName

@bp.route('/index', methods=('GET', 'POST'))
def create():
    curr_city = getLocalCityName()
    weather_data = getWeather(curr_city)
    data = {"city": curr_city, "weather": weather_data}
    return render_template('index/index.html', data = data)
