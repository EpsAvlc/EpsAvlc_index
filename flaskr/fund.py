from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

bp = Blueprint('fund', __name__)


from .crawler.fund_crawler import get_fund_dict
@bp.route('/fund')
def create():
    fund_list = get_fund_dict()
    keys = ['name', 'pb', 'pe', 'roe']
    return render_template('fund/fund.html', fund_list = fund_list, keys = keys)