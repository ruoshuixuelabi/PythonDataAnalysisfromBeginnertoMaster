import pandas as pd

data = [[110, 105, 99], [105, 88, 115], [109, 120, 130], [112, 115, 140]]
name = ['明日', '七月流火', '高袁圆', '二月二']
columns = ['语文', '数学', '英语']
df = pd.DataFrame(data=data, index=name, columns=columns)

# 按行增加数据，增加多行数据
df_insert = pd.DataFrame({'语文': [100, 123, 138], '数学': [120, 142, 60], '英语': [99, 139, 99]},
                         index=['钱多多', '童年', '无名'])
# https://pandas.pydata.org/docs/whatsnew/v2.0.0.html
# Removed deprecated Series.append(), DataFrame.append(), use concat() instead (GH35407)
# df1 = df.append(df_insert)
df1 = pd.concat([df, df_insert])
print(df1)
