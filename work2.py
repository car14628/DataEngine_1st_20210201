

import numpy as np
from pandas import Series, DataFrame

data = {'语文': [68, 95, 98, 90,80], '数学': [65, 76, 86, 88, 90], '英语': [30, 98, 88, 77, 90]}
df = DataFrame(data, index=['ZhangFei', 'GuanYu', 'LiuBei', 'DianWei', 'XuChu'])
print(df)
#print(df.describe())
print("课程=平均成绩=最小成绩=最大成绩===方差=====标准差")
for item in df.columns:
    print("{0:^1} {1:^7} {2:^7} {3:^7} {4:>7.2f} {5:>8.2f}"
          .format(item, np.mean(df[item]), np.min(df[item]), np.max(df[item]), np.var(df[item]), np.std(df[item])))
print("=====================================================")

df["总分"] = df.sum(axis=1)
df1 = df.sort_values("总分", ascending=False)
print("总分排位：")
print(df1)
