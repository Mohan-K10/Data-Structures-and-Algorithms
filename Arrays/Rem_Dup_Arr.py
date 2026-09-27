from array import *

arr = array('i', [0,0,1,1,1,2,2,3,3,4])
i = 0

for j in range(1, len(arr)):
    if arr[j] != arr[i]:
        i = i+1
        arr[i] = arr[j]
    
print(i+1)