import pandas as pd

data = [[110, 105, 99], [105, 88, 115], [109, 120, 130], [112, 115, 140]]
name = ['明日', '七月流火', '高袁圆', '二月二']
columns = ['语文', '数学', '英语']
df = pd.DataFrame(data=data, index=name, columns=columns)
df.index = list('1234')
# 也可以使用rename属性
# df.rename({'明日':1,'七月流火':2,'高袁圆':3,'二月二':4},axis=0,inplace = True)
