import pandas as pd
import numpy as np
df = pd.read_csv('C:/Users/ELCOT/Desktop/excel/PRACTICE-DATA/Data_science.csv', index_col='Name')

#indexing
print(df.loc['Srikanth'].shape)
print(df.loc['Srikanth':'Pravin'])
print(df.iloc[3])
print(df.iloc[1:7])
print(df['Age'].shape)
print(df[['Age','Height']].head(n=3))
print(type(df.loc['Srikanth']))

#Statics
print(df['Age'].mean())
print(df.describe())
print(df.median())
print(df.quantile([0.25,0.5,0.75,1]))
print(df.info())
print(df.var())
print(df.std())
print(df.groupby('Party').mean())
print(df.groupby('Party')['Height'].agg([min,np.median,max]))
print(df.groupby('Party').agg({'Height':[np.median,np.mean],'Age':[min,max]}))