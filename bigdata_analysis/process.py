import pandas as pd
import matplotlib.pyplot as plt

# 导入数据
info_august = pd.read_csv('meal_order_info.csv', encoding='utf-8')
users_august = pd.read_csv('users.csv', encoding='gbk')


# 提取订单状态为1的数据
info_august_new = info_august[info_august['order_status'].isin([1])]
info_august_new = info_august_new.reset_index(drop=True)
# print('提取的订单数据维数：', info_august_new.shape)
# info_august_new.to_csv('info_august_new.csv', index=False, encoding='utf-8')


# 匹配用户的最后一次用餐时间
for i in range(1, len(info_august_new)):
    num = users_august[users_august['USER_ID'] ==
                       info_august_new.iloc[i-1, 1]].index.tolist()
    users_august.iloc[num[0], 14] = info_august_new.iloc[i-1, 9]

user = users_august
user['LAST_VISITS'] = user['LAST_VISITS'].fillna(999)
user = user.drop(user[user['LAST_VISITS'] == 999].index.tolist())
user = user.iloc[:, [0, 2, 12, 14]]
print(user.head())
user.to_csv('users_august.csv', index=False, encoding='utf-8')


