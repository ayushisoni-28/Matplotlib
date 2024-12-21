import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#2 D line plot
# used in bivariate analysis
# numerical as well as categorical
#use case- time series data
'''
#suppose we have stock sales yr wise
x=[20000,30000,34440,75555]#sales(numerical)
y=[2019,2020,2021,2022]#year(categorical)

#now plot (x axis, yaxis) (categorical,numerical)
plt.plot(y,x)
print(plt.show()) 

'''

batsman=pd.read_csv('file data path') #copy the path of data
print(batsman)
 #color... line-width...line-style....legend label...marker
plt.plot(batsman['index'],batsman['V Kohli'],color='black',label='Virat',linewidth=3,linestyle='dashed')
plt.plot(batsman['index'],batsman['RG Sharma'],color='yellow',label='Rohit',linewidth=3,marker='D')

#now lets title the graph for better understanding
plt.title('Rohit sharma V/S Virat Kohli IPL Runs')

plt.xlabel('Year')

plt.ylabel('Runs')

# for legend we can set location also upper right.. etc
plt.legend(loc='upper left')

plt.show()


