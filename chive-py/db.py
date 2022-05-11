import pymysql
import config


def execsql(sql):
    db = pymysql.connect(host='127.0.0.1',
                         user=config.get('db_user'),
                         passwd=config.get('db_passwd'),
                         db=config.get('db'),
                         charset='utf8')
    cursor = db.cursor()

    try:
        cursor.execute(sql)
        db.commit()
        db_ret = cursor.fetchall()
    except pymysql.Error as e:
        # db.rollback()
        print(e.args)
        return False
    finally:
        db.close()

    return db_ret