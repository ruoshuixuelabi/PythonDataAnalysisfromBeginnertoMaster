import pandas as pd
import matplotlib.pylab as plt

data = [110,105,99,120,115,112,118,120,109,113]
index=[1,2,3,4,5,6,7,8,9,10]
df = pd.DataFrame(data=data,index=index,columns=['英语'])
df['升降']=df['英语']-df['英语'].shift()
print(df)
df['升降'].plot(style='b')
plt.show()