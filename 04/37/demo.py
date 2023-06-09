import pandas as pd

df1 = pd.DataFrame({'编号':['mr001','mr002','mr003'],
                    '语文':[110,105,109],
                    '数学':[105,88,120],
                    '英语':[99,115,130]})

df2 = pd.DataFrame({'编号':['mr001','mr002','mr003'],
                    '体育':[34.5,39.7,38]})

df_merge=pd.merge(df1,df2,left_index=True,right_index=True)
print(df_merge)
