import threading
import datetime
import json

import db
import source_data as sd

track_set = set()
cur_day = datetime.datetime.now() - datetime.timedelta(days=365)


def load() -> bool:
    '''Load track list from MySQL'''

    global track_set

    sql_load = """
    SELECT * FROM track_list
    """
    ret = db.execsql(sql_load)
    if ret == False:
        return False

    for stock_code in ret:
        track_set.add((stock_code[0]))

    return True


def get_start_time():
    now_time = datetime.datetime.now()
    # 获取明天时间
    # next_time = now_time + datetime.timedelta(days=+1)
    next_time = now_time

    # 获取明天起始时间点
    next_time = datetime.datetime.strptime(
        str(next_time.date().year) + "-" + str(next_time.date().month) + "-" +
        str(next_time.date().day) + " 02:14:00", "%Y-%m-%d %H:%M:%S")

    # 获取距离明天时间，单位为秒
    timer_start_time = (next_time - now_time).total_seconds()
    return timer_start_time


def set_next_loop(default_interval=3):
    timer = threading.Timer(default_interval, track_once)
    timer.start()
    return


def track_once():
    '''query from tushare, save in MySQL'''

    global cur_day
    st = cur_day.strftime('%Y%m%d')
    et = cur_day + datetime.timedelta(days=1)
    et = et.strftime('%Y%m%d')

    print('\nCurrent Day(mock): ', st)
    sd.get_source_data(track_set, st, et)

    cur_day += datetime.timedelta(days=1)

    # need recursive call
    set_next_loop()
    return


def init():
    try:
        if not load():
            return False
        start_time = get_start_time()

        first_loop = threading.Timer(start_time, track_once)
        first_loop.start()
        return True
    except Exception as e:
        print(e)
        return False


def add_stock(stock_code: str) -> bool:
    global track_set

    if stock_code in track_set:
        return False

    sql_insert = """
    INSERT INTO 
    track_list (stock_code)
    VALUES ('%s');
    """ % (stock_code)

    ret = db.execsql(sql_insert)
    if ret == False:
        print('inner ERROR')
        return False

    track_set.add(stock_code)

    return True


def del_stock(stock_code: str) -> bool:
    global track_set

    if stock_code not in track_set:
        return False

    sql_delete = """
    DELETE FROM track_list
    WHERE stock_code = '%s';
    """ % (stock_code)

    ret = db.execsql(sql_delete)
    if ret == False:
        print('inner ERROR')
        return False

    track_set.remove(stock_code)

    return True


def get_track_list() -> set:
    return track_set


def check_count(stock_code: str) -> bool:
    '''检查有无最近20条数据'''

    et = cur_day.strftime('%Y-%m-%d')
    st = cur_day - datetime.timedelta(days=40)
    st = st.strftime('%Y-%m-%d')
    print(st, et)
    sql_search = """
    SELECT * FROM stock_all 
    WHERE stock_code = '%s' and state_dt >= '%s' and state_dt <= '%s';
    """ % (stock_code, st, et)

    ret = db.execsql(sql_search)
    if ret == False:
        print('inner ERROR')
        return False

    if len(ret) < 20:
        return False

    return True


if __name__ == '__main__':
    print('test')

    # timer = threading.Timer(timer_start_time, track)
    # timer.start()
    # while True:
    #     print("1s")
    #     time.sleep(1)