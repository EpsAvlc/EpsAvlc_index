from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

bp = Blueprint('fund', __name__)

valuation_site = 'https://danjuanapp.com/djmodule/value-center'

@bp.route('/fund')
def create():
    return render_template('fund/fund.html', cols = {1, 2}, rows = {1, 2})