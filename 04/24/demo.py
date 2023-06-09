import pandas as pd  #导入pandas模块
#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
df=pd.read_csv('JD.csv',encoding='gbk')  #导入csv文件
df=df.set_index(['商品名称'])
data={'北京出库销量':'北上广','上海出库销量':'北上广',
         '广州出库销量':'北上广','成都出库销量':'成都',
         '武汉出库销量':'武汉','西安出库销量':'西安',}
s1=pd.Series(data)
print(s1)
df1=df.groupby(s1,axis=1).sum()
print(df1)


