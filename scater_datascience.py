import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

df = pd.read_csv('C:/Users/ELCOT/Desktop/excel/PRACTICE-DATA/Data_science.csv',index_col='Name')
plt.scatter(df['Height'],df['Age'], marker='*', color='k')
plt.xlabel('height')
plt.ylabel('age')
plt.title('Height and name')
plt.show() 

df.plot(kind = 'scatter', x='Height', y='Age', title='Height and age')
plt.show()

plt.hist(df['Height'],bins=5)
plt.show()