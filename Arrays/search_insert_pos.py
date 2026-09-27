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

# Merge sorted array

nums1 = [1, 2, 3, 0, 0 ,0]
nums2 = [2, 5, 6]
m = 3
n = 3
i = m - 1
j = n - 1
k = len(nums1) - 1

while i >= 0 and j >= 0:
    if nums1[i] > nums2[j]:
        nums1[k] = nums1[i]
        k = k - 1
        i = i - 1
    else :
        nums1[k] = nums2[j]
        k = k - 1
        j = j - 1
while j >= 0:
    nums1[k] = nums2[j]
    k -= 1
    j -= 1
print(nums1)