from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

bp = Blueprint('fund_grid', __name__)

@bp.route('/fund_grid')
def create():

    return render_template("fund/fund_grid.html")


