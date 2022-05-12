import csv
import config
import db

if __name__ == '__main__':
    config.init()

    sql_search = """
    SELECT * FROM stock_all 
    WHERE stock_code = '{}' and state_dt >= '{}' and state_dt <= '{}' 
    ORDER BY state_dt ASC
    """.format('603912.SH', '20150101', '20220401')

    #  '603912.SH', '300666.SZ', '300618.SZ', '002049.SZ', '300672.SZ'

    ret = db.execsql(sql_search)
    if ret == False:
        print("inner ERROR")
        exit()

    print(ret)
    print(len(ret))
    
    # with open("data.csv", "w") as csvfile:
    #     writer = csv.writer(csvfile)

    #     # set columns name
    #     writer.writerow([
    #         "state_dt",
    #         "stock_code",
    #         "open",
    #         "close",
    #         "high",
    #         "low",
    #         "vol",
    #         "amount",
    #         "pre_close",
    #         "amt_change",
    #         "pct_change",
    #     ])

    #     # write data
    #     writer.writerows(ret)