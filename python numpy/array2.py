import numpy as np


arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])

# for x in arr:
#   for y in x:
#     print([x,y])

# l =len(arr)

# print(l)
for x in range(len(arr)):
  for y in range(len(arr[x])):
    print([x,y]," = ",arr[x][y])
    
    
    