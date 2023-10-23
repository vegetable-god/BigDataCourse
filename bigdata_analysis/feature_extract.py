import pandas as pd
from  sklearn.preprocessing import StandardScaler
import numpy as np

info = pd.read_csv('info_august_new.csv', encoding='utf-8')
user = pd.read_csv('users_august.csv', encoding='utf-8')


# 统计每个人的用餐次数
user_value1 = pd.DataFrame(info['emp_id'].value_counts()).reset_index()
user_value1.columns = ['USER_ID', 'F']
# print('F特征的最大值：', max(user_value1['F']))
# print('F特征的最小值：', min(user_value1['F']))


# 构建M特征
user_value2 = info[['emp_id', 'expenditure']].groupby(by='emp_id').sum()
user_value2 = pd.DataFrame(user_value2).reset_index()
user_value2.columns = ["USER_ID", "M"]
user_value = pd.merge(user_value1, user_value2, on='USER_ID')
# print('M特征的最大值：', max(user_value['M']))
# print('M特征的最小值：', min(user_value['M']))


# 构建R特征
user_value = pd.merge(user_value, user, on='USER_ID')
for i, k in enumerate(user_value['LAST_VISITS']):
    y = k.split()
    y = pd.to_datetime(y[0])
    user_value.loc[i, 'LAST_VISITS'] = y
last_time = pd.to_datetime(user_value['LAST_VISITS'])
deadline = pd.to_datetime("2016-8-31")
user_value['R'] = deadline - last_time
# print('R特征的最大值：', max(user_value['R']))
# print('R特征的最小值：', min(user_value['R']))


# 特征提取
user_value = user_value.iloc[:, [0, 3, 6, 1, 2]]

USER_ID = user_value['USER_ID']
ACCOUNT = user_value['ACCOUNT']
user_value = user_value.iloc[:, [2, 3, 4]]
user_value.iloc[:, 0] = [i.days for i in user_value.iloc[:, 0]]

# 标准差标准化
standard = StandardScaler().fit_transform(user_value)
# np.savez('standard.npz', standard)
print(standard)
