from flask import Flask, request, Response
import pymysql
import json
import config

input_error = lambda: Response({'msg': 'req recieved, input error'}, 200)
inner_error = lambda: Response({'msg': 'req recieved, inner error'}, 200)

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/data")
def get_stock_data():
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

if __name__ == '__main__':

    config.init()

    app.run()