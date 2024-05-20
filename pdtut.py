import pandas as pd
import re
import matplotlib as mat
import numpy as np
d = [{'data_gmt':{'a': 6, 'b': 4, 'c': 5}},{'data_gmt':{'a': 1, 'b': 2, 'c': 3}}]

ser = pd.Series(data=d[0]['data_gmt'], index=['a', 'b', 'c'])
print(ser)
ser = pd.Series(data=d[0]['data_gmt'], index=['x', 'y', 'z'])
print(ser)

df1 = pd.DataFrame(d[0]['data_gmt'], index=["row1", "row2", "row3"])
print(df1)
df = pd.read_csv('panddata/data1.csv')
df.plot()
# mat.pyplot.show()#default plot

df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')#Scatter Plot
# mat.pyplot.show()

df.plot(kind = 'hist', x = 'Duration')#Scatter Plot
# mat.pyplot.show()#Hisogram plot

cor = df.corr()
print(cor)
print(df.index)
df.at[4,'Duration'] = 0 if df.at[4,'Duration'] == 45 else '' #get and replace value at
print(df)
daterange = pd.date_range(start='1/12/2022',end='12/12/2028', freq='M')
print(daterange)#last dates of every month between start and end date
print(np.sum(df, axis=0))
print(np.mean(df, axis=0))

df1 = pd.DataFrame(np.array([
    ['a', 5, 9],
    ['b', 4, 61],
    ['c', 24, 9]]),
    columns=['name', 'attr11', 'attr12'])
df2 = pd.DataFrame(np.array([
    ['a', 5, 19],
    ['b', 4, 16],
    ['c', 24, 9]]),
    columns=['name', 'attr21', 'attr22'])
df3 = pd.DataFrame(np.array([
    ['a', 15, 49],
    ['b', 4, 36]]),
    columns=['name', 'attr31', 'attr32'])

df4 = [df1, df2, df3] #List of dataframes
concatpd = pd.concat(df4, sort=False, axis=1) #Concat mutiple dataframe of same type
concatpd = concatpd.loc[:, ~concatpd.columns.duplicated()] #Remove duplicate column names and keep first column only
print(concatpd)
