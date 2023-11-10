heights = [1,2,3,4,5,6,7,8,9,10,1,1,11,33,44,3,4,56,56,5644,4,44,]

cnt = 0 
for height in heights:
    if height >10:
        cnt+=1
print(cnt)

#this set is in datascience
import numpy as np 
heights_arr = np.array(heights)
print((heights_arr > 10).sum())
print(heights_arr.shape)

#new list
ages = [22,33,44,55,66,77,88,11,33,55,44,66,66,44,55,66,77,88,33,44,55,56,]
heights_and_ages = heights+ages
heights_and_ages = np.array(heights_and_ages)
print(heights_and_ages.shape)

#reshaping
print(heights_and_ages.reshape((2,22)))

#datatype
h = [1.0,2,3,4,5,6,7,8,9,10,1,1,11,33,44,3,4,56,56,5644,4,44,]
h_arr = np.array(h)
print(h_arr.dtype)

#3.INDEXING AND SLICING IN NUMPY

print(heights_arr[2])
heights_and_ages_arr=heights_and_ages.reshape((2,22))
print(heights_and_ages_arr[1,2])
print(heights_and_ages_arr[0:2,0])

#ASSIGNING VALUES
heights_and_ages_arr[:1,:2]=0
print(heights_and_ages_arr)

#ASSIGN A VALUE
new_record = np.array([[180,183,190],[54,55,56]])
heights_and_ages_arr = heights_and_ages_arr.reshape((2,22))
heights_and_ages_arr[:,19:]= new_record
print(heights_and_ages_arr)

ages_arr = np.array(ages)
heights_arr = heights_arr.reshape((22,1))
print(heights_arr)

print(heights_and_ages_arr[0,:] * 0.328084)
