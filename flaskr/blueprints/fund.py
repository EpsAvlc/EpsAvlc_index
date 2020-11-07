from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

bp = Blueprint('fund', __name__)


from ..crawler.fund_crawler import get_fund_dict
@bp.route('/fund')
def create():
    fund_list = get_fund_dict()
    keys = ['name', 'pb', 'pe', 'roe', 'eva_type_int']
    keys_chinese = {'name': '指数名称', 'pb':'市净率', 'pe': '市盈率', 'roe':'净资产收益率', 'eva_type_int': '估值'}
    return render_template('fund/fund.html', fund_list = fund_list, keys = keys, keys_chinese = keys_chinese)