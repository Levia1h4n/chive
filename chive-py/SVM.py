from sklearn import svm
import DC
import config

if __name__ == '__main__':

    config.init()

    # 输入端的数据是个股每日基础行情, 输出端数据是股价相较前一交易日的涨跌状态
    stock = '002049.SZ'
    dc = DC.data_collect(stock, '2020-03-01', '2022-03-01')
    # self.train: 训练集中的输入端数据, 本例中是每日基础行情
    # self.target: 训练集中的输出数据, 本例中相较于前一天股价的涨跌, 涨为1, 不涨为0。
    #              并且在排序上, 每条 t 交易日的self.train里的数据对应的是 t+1 天股价的涨跌状态
    # self.test_case: 在 t 末交易日的基础行情数据, 作为输入端, 用于模型训练完成后, 对第二天的涨跌进行预测
    train = dc.data_train
    target = dc.data_target
    test_case = [dc.test_case]

    model = svm.SVC()  # 建模
    model.fit(train, target)  # 训练
    res = model.predict(test_case)  # 预测

    # 输出对2020-03-02的涨跌预测, 1表示涨, 0表示不涨。-1?
    print(res[0])
