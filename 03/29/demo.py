import pandas as pd

data = [[110, 105, 99], [105, 88, 115], [109, 120, 130], [112, 115, 140]]
name = ['明日', '七月流火', '高袁圆', '二月二']
columns = ['语文', '数学', '英语']
df = pd.DataFrame(data=data, index=name, columns=columns)

# 按行增加数据，增加一行数据
df.loc['钱多多'] = [100, 120, 99]
print(df)
