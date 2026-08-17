from array import *

arr = array('i', [1, 2, 3, 4, 5])

for x in arr:
    print(x, end=" ")
print('\n')
search_index = arr.index(int(input("Enter the number to search from array: ")))

print(search_index)



# Dynamically enter array values from user

# arr = array('i', [])

# arr_size = int(input("Enter the size of array: "))

# for i in range(0, arr_size):
#     arr.append(int(input("Enter the array value: ")))

# for x in arr:
#     print(x, end=" ")



# copy array

# val = array('i', [1, 2, 3, 4, 5, 6])

# print("Typecode: ", val.typecode)
# copyArray = array(val.typecode, (x for x in val))
# print("Copy Array: ")

# for i in range(0, len(val)):
#     print(copyArray[i], end=" ")



# for i in range(0, len(val)):
#     print(val[i], end=" ")

# print('\n')
# print("Without range function: ")

# for x in val:
#     print(x, end="  ")

# print('\n')
# print(val.typecode) # typecode -> tells which type of array in code form (i, h...)

# Reverse an array by using reverse()
# val.reverse()
# val.insert(2, 40)

# print('\n')
# for i in range(0, len(val)):
#     print(val[i], end=" ")