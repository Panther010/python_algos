# Python program to find an element x
# in a sorted array using Exponential Search

def binary_search(arr, begining, length, x):

    if length >= begining:

        mid = (begining + length ) //2
        print(arr, begining, length, x, mid)
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return binary_search(arr, mid+1, length, x)
        else:
            return binary_search(arr, begining, mid-1, x)
    else:
        return -1

def exponential_search(arr, length, x):
    if arr[0] == x:
        return 0

    i = 1
    while i < length and arr[i]<= x:
        if arr[i] == x:
            return i
        i =i*2

    return binary_search(arr, i//2, min(i,length-1), x)

arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
x = 24
length = len(arr)

result = exponential_search(arr, length, x)
#result = binary_search(arr, 0, length-1, x)
print(result)