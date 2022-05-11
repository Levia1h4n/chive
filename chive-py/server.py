from flask import Flask, request, Response
from flask_cors import CORS
import pymysql
import json
import copy

import config
import asset

input_error = lambda msg: Response(json.dumps(
    {'msg': 'req recieved, invalid input' if len(msg) == 0 else msg}),
                                   200,
                                   mimetype='application/json')
inner_error = lambda: Response(json.dumps({'msg': 'req recieved, inner error'}
                                          ),
                               200,
                               mimetype='application/json')

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/test/get")
def testGet():
    a = request.args.get('arg')
    print(a)
    if a == '1':
        ret = json.dumps({'msg': 'test data', 'data': [1, 2, 3, 4]})
    else:
        ret = json.dumps({'msg': 'test data', 'data': [4, 3, 2, 1]})
    # response.setHeader("Access-Control-Allow-Origin", "*")
    return Response(response=ret, status=200, mimetype='application/json')


@app.route("/source")
def get_source_data():
    '''获取源数据'''
    pass


@app.route("/asset")
def get_asset():
    '''获取个人资产'''
    acct = request.args.get('acct')
    pwd = request.args.get('pwd')
    if acct not in asset.account_pool or not asset.check_pwd(acct, pwd):
        return input_error('acct and pws not match')

    ret = copy.deepcopy(asset.account_pool[acct])
    del ret['pwd']
    ret = json.dumps({'msg': 'succ', 'data': ret})
    return Response(response=ret, status=200, mimetype='application/json')


@app.route("/buy")
def get_buy():
    acct = request.args.get('acct')
    pwd = request.args.get('pwd')
    stock_code = request.args.get('stock_code')
    amount = request.args.get('amount')

    if not asset.check_pwd(acct, pwd):
        return input_error('acct and pwd not match')

    succ = asset.buy(acct, pwd, stock_code, amount)
    if not succ:
        return inner_error()

    return Response(json.dumps({'msg': 'succ'}),
                    200,
                    mimetype='application/json')


@app.route("/sell")
def get_sell():
    acct = request.args.get('acct')
    pwd = request.args.get('pwd')
    stock_code = request.args.get('stock_code')
    amount = request.args.get('amount')

    if not asset.check_pwd(acct, pwd):
        return input_error('acct and pwd not match')

    succ = asset.sell(acct, pwd, stock_code, amount)
    if not succ:
        return inner_error()

    return Response(json.dumps({'msg': 'succ'}),
                    200,
                    mimetype='application/json')


@app.route("/data")
def get_stock_data():
    '''画k线图'''
    # GET parameter
    stock_code = request.args.get('stock_code')
    date_from = request.args.get('date_from')
    date_to = request.args.get('date_to')

    if not (stock_code and date_from and date_to):
        return input_error()

    print('get_stock_data(): ', stock_code, date_from, date_to)

    sql_search = """
    SELECT * FROM stock_all 
    WHERE stock_code = '{}' and state_dt >= '{}' and state_dt <= '{}' 
    ORDER BY state_dt ASC
    """.format(stock_code, date_from, date_to)

    db = pymysql.connect(host='127.0.0.1',
                         user=config.get('db_user'),
                         passwd=config.get('db_passwd'),
                         db=config.get('db'),
                         charset='utf8')
    cursor = db.cursor()

    try:
        cursor.execute(sql_search)
        db_ret = cursor.fetchall()
    except pymysql.Error as e:
        print(e.args)
        return inner_error()
    finally:
        db.close()

    ret = json.dumps({'data': db_ret})
    return Response(response=ret, status=200, mimetype='application/json')


# @app.route('/data', methods=['GET', 'POST'])
# def abd():
#     if request.method == 'POST':
#         print('post')
#         print(request.content_type)
#         print(request.form)
#     elif request.method == 'GET':
#         print('get')
#         print(request.content_type)
#         print(request.args.get('name'))
#         print(request.args.get('ok'))
#     return "<p>Hello, World!</p>"

# CORS(app, supports_credentials=True)
CORS(app, resources=r'/*')

# @app.after_request
# def cors(environ):
#     environ.headers['Access-Control-Allow-Origin'] = '*'
#     environ.headers['Access-Control-Allow-Method'] = '*'
#     environ.headers[
#         'Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
#     return environ


def after_request(resp: Response) -> Response:
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Method'] = '*'
    resp.headers[
        'Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return resp


# app.after_request(after_request)
# app.before_request(after_request)

# flask run / python3 server.py
# config.init()

if __name__ == '__main__':
    # 'flask run' cannot load the config in this way
    config.init()

    succ = asset.load()
    if not succ:
        print('Load ERROR')
        exit()

    app.run()