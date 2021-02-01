import pandas as pd

#导入源数据
df = pd.read_csv('car_complain.csv')
#将品牌名称统一
def f(x):
    x = x.replace('一汽-大众','一汽大众')
    return x
df['brand'] = df['brand'].apply(f)
#print(df)
#将问题类型拆分，有无用“0”，“1”表示
df = df.drop('problem',axis=1).join(df.problem.str.get_dummies(','))
#print(df1)

#品牌投诉总数排序
df1 = df.groupby(['brand'])['id'].agg(['count']).sort_values('count', ascending = False)
df1.reset_index(inplace=True)
print('————————品牌投诉总数排序————————')
print(df1)

#车型投诉总数排序
df2 = df.groupby(['car_model'])['id'].agg(['count']).sort_values('count', ascending = False)
df2.reset_index(inplace=True)
print('————————车型投诉总数排序————————')
print(df2)

#品牌平均车型投诉排序
df3 = df.groupby(['car_model','brand'])['id'].agg(['count'])
df3 = df3.groupby(['brand']).mean().sort_values('count', ascending = False)
df3.reset_index(inplace=True)
print('———————品牌平均车型投诉排序———————')
print(df3)

