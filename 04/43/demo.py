import pandas as pd

data = [['a',110,105,99],['b',105,88,115],['c',109,120,130],['d',112,115]]
index = [1,2,3,4]
columns = ['A','语文','数学','英语']
df1 = pd.DataFrame(data=data, index=index, columns=columns)

df1.to_excel('df1.xlsx',sheet_name='df1')
work=pd.ExcelWriter('df2.xlsx')  #打开一个Excel文件
df1.to_excel(work,sheet_name='df2')
df1['A'].to_excel(work,sheet_name='df3')
work.save()
