import datetime
import tushare as ts
import pymysql

import config


def get_source_data(stocks, start_dt='20150101', end_dt=''):
    ts.set_token(config.get('token'))
    pro = ts.pro_api()
    # 设定获取日线行情的初始日期和终止日期，其中终止日期设定为昨天。
    if end_dt == '':
        time_temp = datetime.datetime.now() - datetime.timedelta(days=1)
        end_dt = time_temp.strftime('%Y%m%d')

    # 建立数据库连接,剔除已入库的部分
    db = pymysql.connect(host='127.0.0.1',
                         user=config.get('db_user'),
                         passwd=config.get('db_passwd'),
                         db=config.get('db'),
                         charset='utf8')
    cursor = db.cursor()

    # 设定需要获取数据的股票池
    stock_pool = list(stocks)

    total = len(stock_pool)
    # 循环获取单个股票的日线行情
    for i in range(len(stock_pool)):
        try:
            df = pro.daily(ts_code=stock_pool[i],
                           start_date=start_dt,
                           end_date=end_dt)
            # 打印进度
            print('Seq: ' + str(i + 1) + ' of ' + str(total) + '   Code: ' +
                  str(stock_pool[i]))
            c_len = df.shape[0]
        except Exception as aa:
            print(aa)
            print('No DATA Code: ' + str(i))
            continue

        errFlag = True

        for j in range(c_len):
            resu0 = list(df.iloc[c_len - 1 - j])
            resu = []
            for k in range(len(resu0)):
                if str(resu0[k]) == 'nan':
                    resu.append(-1)
                else:
                    resu.append(resu0[k])
            state_dt = (datetime.datetime.strptime(
                resu[1], "%Y%m%d")).strftime('%Y-%m-%d')

            try:
                sql_insert = "REPLACE INTO stock_all (state_dt, stock_code, open, close, high, low, vol, amount, pre_close, amt_change, pct_change) \
                    VALUES ('%s', '%s', '%.2f', '%.2f','%.2f','%.2f','%i','%.2f','%.2f','%.2f','%.2f')" % (
                    state_dt, str(resu[0]), float(resu[2]), float(
                        resu[5]), float(resu[3]), float(resu[4]), float(
                            resu[9]), float(resu[10]), float(
                                resu[6]), float(resu[7]), float(resu[8]))
                cursor.execute(sql_insert)
                db.commit()
            except Exception as err:
                if errFlag:
                    print(err)
                    errFlag = False
                continue
    cursor.close()
    db.close()

    print('All Finished!')


if __name__ == '__main__':

    config.init()

    # 设置tushare pro的token并获取连接
    ts.set_token(config.get('token'))
    pro = ts.pro_api()
    # 设定获取日线行情的初始日期和终止日期，其中终止日期设定为昨天。
    start_dt = '20150101'
    time_temp = datetime.datetime.now() - datetime.timedelta(days=1)
    end_dt = time_temp.strftime('%Y%m%d')

    # 建立数据库连接,剔除已入库的部分
    db = pymysql.connect(host='127.0.0.1',
                         user=config.get('db_user'),
                         passwd=config.get('db_passwd'),
                         db=config.get('db'),
                         charset='utf8')
    cursor = db.cursor()

    # 设定需要获取数据的股票池
    stock_pool = [
        '603912.SH', '300666.SZ', '300618.SZ', '002049.SZ', '300672.SZ'
    ]
    total = len(stock_pool)
    # 循环获取单个股票的日线行情
    for i in range(len(stock_pool)):
        try:
            df = pro.daily(ts_code=stock_pool[i],
                           start_date=start_dt,
                           end_date=end_dt)
            # 打印进度
            print('Seq: ' + str(i + 1) + ' of ' + str(total) + '   Code: ' +
                  str(stock_pool[i]))
            c_len = df.shape[0]
        except Exception as aa:
            print(aa)
            print('No DATA Code: ' + str(i))
            continue

        errFlag = True

        for j in range(c_len):
            resu0 = list(df.iloc[c_len - 1 - j])
            resu = []
            for k in range(len(resu0)):
                if str(resu0[k]) == 'nan':
                    resu.append(-1)
                else:
                    resu.append(resu0[k])
            state_dt = (datetime.datetime.strptime(
                resu[1], "%Y%m%d")).strftime('%Y-%m-%d')

            try:
                sql_insert = "REPLACE INTO stock_all (state_dt, stock_code, open, close, high, low, vol, amount, pre_close, amt_change, pct_change) \
                    VALUES ('%s', '%s', '%.2f', '%.2f','%.2f','%.2f','%i','%.2f','%.2f','%.2f','%.2f')" % (
                    state_dt, str(resu[0]), float(resu[2]), float(
                        resu[5]), float(resu[3]), float(resu[4]), float(
                            resu[9]), float(resu[10]), float(
                                resu[6]), float(resu[7]), float(resu[8]))
                cursor.execute(sql_insert)
                db.commit()
            except Exception as err:
                if errFlag:
                    print(err)
                    errFlag = False
                continue
    cursor.close()
    db.close()

    print('All Finished!')
