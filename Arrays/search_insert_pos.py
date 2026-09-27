from array import *

arr = array('i', [1,3,5,6])
start = 0
end = len(arr) - 1 #3
target = 5
while start <= end:
    mid = (start + end) // 2
    if arr[mid] == target:
        print(mid)
    if arr[mid] < target:
        start = mid + 1
    else:
        end = mid - 1
# if the target is not found, then it will point index where the non existing value must be in array
print(start)