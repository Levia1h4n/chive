from sklearn import svm
import DC
import config

if __name__ == '__main__':

    config.init()
    print(config.cfg)
    
    stock = '002049.SZ'
    dc = DC.data_collect(stock, '2020-03-01', '2022-03-01')
    train = dc.data_train
    target = dc.data_target
    test_case = [dc.test_case]
    model = svm.SVC()               # 建模
    model.fit(train, target)        # 训练
    ans2 = model.predict(test_case) # 预测
    # 输出对2020-03-02的涨跌预测，1表示涨，0表示不涨。
    print(ans2[0])


