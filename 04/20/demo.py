import pandas as pd  #导入pandas模块

df=pd.read_csv('JD.csv',encoding='gbk')
#抽取数据
df1=df[['一级分类','7天点击量','订单预定']]
print(df1.groupby('一级分类').agg(['mean','sum']))





