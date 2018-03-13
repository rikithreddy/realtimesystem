import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



plt.style.use('seaborn')
fig,ax = plt.subplots(figsize=(100,100))


df = pd.read_csv('result.csv')
print df


plt.xlabel('Number of Processors')
plt.ylabel('Migrations')
plt.title('DP Fair vs ER Fair Migrations')
ax.plot(df['p'].values,df['DP'].values,'C1',label='DP Fair')
ax.plot(df['p'].values,df['ER'].values,'C2',label='ER Fair')
ax.legend()


#plt.savefig('result.jpg')
plt.show()

#print df.columns
