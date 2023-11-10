import pandas as pd 
a = 10
print(a)
print(pd.Series({'a':1, 'b':2, 'c':3}))
df = pd.read_csv('C:/Users/ELCOT/Desktop/excel/PRACTICE-DATA/Data_science.csv')
print(df.head(n=3))

wine_dict = { 'red_wine':[3,6,5],'white_wine':[1,2,3,]}
sales = pd.DataFrame(wine_dict,index=["sri", "Ram", "Raja"])
print(sales['white_wine'])

print(df.size)
print(df.head(n=3))
print(df.tail())
df.info()