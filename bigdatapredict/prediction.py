from sklearn.model_selection import  train_test_split
from sklearn.tree import DecisionTreeClassifier as DTC
from sklearn.metrics import confusion_matrix
import pandas as pd
from sklearn.model_selection import GridSearchCV

# from sklearn.datasets import load_digits
# from sklearn.linear_model import Perceptron

from sklearn.datasets import make_hastie_10_2
from sklearn.ensemble import GradientBoostingClassifier

# 划分测试集、训练集
info_user = pd.read_csv('./info_user_clear.csv', encoding='gbk')


# 删除流失用户
info_user = info_user[info_user['type'] != "已流失"]
model_data = info_user.iloc[:, [2, 3, 4, 5, 6]]
# print(model_data.head)
x_tr, x_te, y_tr, y_te = train_test_split(model_data.iloc[:, :-1],
                                          model_data['type'],
                                          test_size=0.2, random_state=12345)


dtc = DTC()
dtc.fit(x_tr, y_tr)
pre = dtc.predict(x_te)
print('预测结果：\n', pre)


# 用GridSearchCV寻找最优参数（字典）
param = {'criterion':['gini', 'log_loss', 'entropy'],'max_depth':[5, 10, 20],'min_samples_leaf':[1, 2, 3],'min_impurity_decrease':[0.01, 0.03, 0.05, 0.08]}
grid = GridSearchCV(dtc,param_grid=param,cv=6)
grid.fit(x_tr, y_tr)
print('最优分类器:',grid.best_params_,'最优分数:', grid.best_score_)  # 得到最优的参数和分值



# clf = Perceptron(penalty='l2', tol=1e-3, random_state=0)
# clf.fit(x_tr, y_tr)
# Perceptron()
# # clf.score(x_tr, y_tr)
# pre = clf.predict(x_te)


# clf = GradientBoostingClassifier(n_estimators=100, learning_rate=0.6,
#                                  max_depth=2).fit(x_tr, y_tr)
# pre = clf.predict(x_te)
# print('预测结果：\n', pre)

# # 混淆矩阵
# hx = confusion_matrix(y_te, pre, labels=['非流失', '准流失'])
# print('混淆矩阵：\n', hx)
#
# # 精确率
# P = hx[1, 1] / (hx[0, 1] + hx[1, 1])
# print('精确率：', round(P, 3))
# # 召回率
# R = hx[1, 1] / (hx[1, 0] + hx[1, 1])
# print('召回率：', round(R, 3))
# # F1值
# F1 = 2 * P * R / (P + R)
# print('F1值：', round(F1, 3))
