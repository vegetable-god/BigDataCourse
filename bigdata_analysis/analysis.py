import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


standard = np.load('standard.npz')['arr_0']
k = 3

# 构建模型
kmeans_model = KMeans(n_clusters=k, n_jobs=3, random_state=123) # 构建聚类器
fit_kmeans = kmeans_model.fit(standard)     # 聚类
# print('聚类中心：\n', kmeans_model.cluster_centers_)

# print('样本的类别标签：\n', kmeans_model.labels_)

# 统计不同类别样本的数目
r1 = pd.Series(kmeans_model.labels_).value_counts()
# print('最终每个类别的数目为：\n', r1)


# angles = np.array([0, 120, 240, 360])
# angles = [0, 120, 240, 360]
angles = 10

# 绘图
fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, polar=True)
sam = ['r', 'g', 'b']
lstype = ['-', '--', '-.']
lab = []
for i in range(len(kmeans_model.cluster_centers_)):
    values = kmeans_model.cluster_centers_[i]
    feature = ['R', 'F', 'M']
    values = np.concatenate((values, [values[0]]))
    # 绘制折线图
    ax.plot(angles, values, sam[i], linestyle=lstype[i], linewidth=2, markersize=10)
    ax.fill(angles, values, alpha=0.5)  # 填充颜色
    ax.set_thetagrids(angles * 180 / np.pi, feature, fontsize=15)  # 添加每个特征的标签
    plt.title('客户群特征分布图')  # 添加标题
    ax.grid(True)
    lab.append('客户群' + str(i + 1))
plt.legend(lab)
plt.show()
plt.close


