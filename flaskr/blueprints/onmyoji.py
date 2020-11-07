from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)


bp = Blueprint('onmyoji', __name__)

@bp.route('/onmyoji', methods=('GET', 'POST'))
def create():
    return render_template('onmyoji/onmyoji.html')