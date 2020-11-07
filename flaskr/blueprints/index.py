from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)


bp = Blueprint('index', __name__)

@bp.route('/index', methods=('GET', 'POST'))
def create():
    import time
    time_tuple = time.localtime(time.time())
    time_dict = {"year":time_tuple.tm_year, "month": time_tuple.tm_mon, "mday": time_tuple.tm_mday}
    return render_template('index/index.html', time_dict = time_dict)