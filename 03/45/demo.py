import pandas as pd

df = pd.read_excel('TB2018.xls')
print(df)
df1 = df.dropna()
print(df1)
df2 = df.dropna().reset_index(drop=True)
print(df2)