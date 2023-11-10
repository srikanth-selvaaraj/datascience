import numpy as np
num_1 = [1,2,3,4,5,6,7,8,9,10]
num_2 = [11,22,33,44,55,66,77,88,99,00]

num_1_arr = np.array(num_1)
num_2_arr = np.array(num_2)

num_1_arr = num_1_arr.reshape((10,1))
num_2_arr = num_2_arr.reshape((10,1))

num_total = np.concatenate((num_1_arr,num_2_arr),axis = 1)
print(num_total)

z = (num_total[:,0] < 5) & (num_total[:,1]<55)
print(num_total[z,])

import pandas as pd
print(10 + 29)