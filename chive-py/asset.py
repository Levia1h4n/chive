import json, hashlib

import config
import db

# e.g.
# acct: 'aaa', pwd: 'bbb'
# {'aaa': {'stocks': {},
#          'pwd': '2ce109e9d0faf820b2434e166297934e6177b65ab9951dbc3e204cad4689b39c'}
account_pool = {}


def load() -> bool:
    '''Load user info from MySQL'''

    global account_pool

    sql_load = """
    SELECT * FROM user_info
    """
    ret = db.execsql(sql_load)
    if ret == False:
        return False

    for user, stocks, pwd in ret:
        account_pool[user] = {'stocks': json.loads(stocks), 'pwd': pwd}
    return True


def set_account(acct='', pwd='') -> bool:
    if acct == '' or pwd == '':
        print('need a valid input')
        return False

    sql_exist = '''
    SELECT 1 FROM user_info WHERE user_acct = '{}' LIMIT 1
    '''.format(acct)

    ret = db.execsql(sql_exist)
    if ret == False or len(ret) != 0:
        print('already EXIST account')
        return False

    sql_insert = """
    INSERT INTO 
    user_info (user_acct, stock_pool, pwd)
    VALUES ('%s', '%s', '%s');
    """ % (acct, json.dumps(dict()), get_hash(acct, pwd))

    ret = db.execsql(sql_insert)
    if ret == False:
        print('inner ERROR')
        return False
    return True


def check_pwd(acct: str, pwd: str) -> bool:
    if get_hash(acct, pwd) == account_pool[acct]['pwd']:
        return True
    else:
        return False


def buy(acct: str, pwd: str, stock_code: str, amount: int) -> bool:
    if acct not in account_pool or not check_pwd(acct, pwd):
        return False

    stocks = account_pool[acct]['stocks']
    cur_amount = stocks.get(stock_code, 0)
    stocks[stock_code] = str(int(cur_amount) + int(amount))

    sql_update = """
    UPDATE user_info 
    SET    stock_pool = '%s'
    WHERE  user_acct = '%s';
    """ % (json.dumps(stocks), acct)

    ret = db.execsql(sql_update)
    if ret == False:
        print('inner ERROR')
        return False

    account_pool[acct]['stocks'] = stocks

    return True


def sell(acct: str, pwd: str, stock_code: str, amount: int) -> bool:
    if acct not in account_pool \
        or stock_code not in account_pool[acct]['stocks'] \
        or amount > account_pool[acct]['stocks'][stock_code] \
        or not check_pwd(acct, pwd):
        return False

    stocks = account_pool[acct]['stocks']
    cur_amount = stocks.get(stock_code)
    stocks[stock_code] = str(int(cur_amount) - int(amount))

    sql_update = """
    UPDATE user_info 
    SET    stock_pool = '%s'
    WHERE  user_acct = '%s';
    """ % (json.dumps(stocks), acct)

    ret = db.execsql(sql_update)
    if ret == False:
        print('inner ERROR')
        return False

    account_pool[acct]['stocks'] = stocks

    return True


def get_hash(acct: str, pwd: str) -> str:
    return hashlib.sha256((acct + pwd).encode('utf-8')).hexdigest()


if __name__ == '__main__':
    # test
    config.init()

    # set_account("aaa", "bbb")
    # set_account("bbb", "aaa")

    load()

    # print(get_hash("abc", "abcd"))
    # print(len(get_hash("abc", "abcd")))

    # print(check_pwd('aaa', 'bbb'))
    # print(check_pwd('aaa', 'aaa'))

    # print('res: ', buy('bbb', 'ccc', 'SH001', 100))
    # print('res: ', buy('bbb', 'aaa', 'SZ001', 100))
    # print('res: ', sell('bbb', 'aaa', 'SZ001', 300))
    # print('res: ', sell('bbb', 'aaa', 'SZ001', 100))

    print(account_pool)