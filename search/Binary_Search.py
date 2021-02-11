# Python3 Program for recursive binary search.
# Returns index of x in arr if present, else -1

def binary_search(arr, begining, length, x):

    if length >= begining:

        mid = (begining + length ) //2
        #print(arr, begining, length, x, mid)
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return binary_search(arr, mid+1, length, x)
        else:
            return binary_search(arr, begining, mid-1, x)
    else:
        return -1

arr = [10, 20, 30, 50, 60, 80, 100, 110, 130, 170, 180]

x = 170
length = len(arr) -1
begining = 0

result = binary_search(arr, begining, length, x)
print(result)