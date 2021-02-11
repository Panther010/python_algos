# Python3 code to linearly search x in arr[].
# If x is present then return its location,
# otherwise return -1

def binary_search(arr, x):
    length = len(arr)
    # search one by one once result matched return the index
    for i in range(length):
        if arr[i] == x:
            return i
    return -1

arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
x = 50

result = binary_search(arr, x)
print(result)