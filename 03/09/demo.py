import pandas as pd

data = [[110, 105, 99], [105, 88, 115], [109, 120, 130]]
index = [0, 1, 2]
columns = ['语文', '数学', '英语']
df = pd.DataFrame(data=data, index=index, columns=columns)
print(df)
# 遍历DataFrame表格数据的每一列
for col in df.columns:
    series = df[col]
    print(series)
