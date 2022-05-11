import json

import config
import db


class Account:

    def __init__(self, acct: str) -> None:
        self.stock_pool = {}


account_pool = {}


def load() -> bool:
    global account_pool

    sql_load = """
    SELECT * FROM user_info
    """
    ret = db.execsql(sql_load)
    if ret == False:
        return False

    for user, stock in ret:
        account_pool[user] = json.loads(stock)
    return True


def set_account(acct='') -> bool:
    if acct == '':
        print('need a valid acct')
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
    user_info (user_acct, stock_pool)
    VALUES ('%s', '%s');
    """ % (acct, json.dumps(dict()))

    ret = db.execsql(sql_insert)
    if ret == False:
        print('inner ERROR')
        return False
    return True


def buy(stock_code: str, accountID: str, amount: int) -> bool:
    pass


def sell(stock_code: str, accountID: str, amount: int) -> bool:
    pass


if __name__ == '__main__':
    # test
    config.init()

    set_account("aaa")

    load()

    print(account_pool)