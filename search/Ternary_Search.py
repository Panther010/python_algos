# Python program to find an element x
# in a sorted array using Ternary Search

def ternary_search(arr, start, length, x):
    if start <= length:
        mid1 = start + (length - start) // 3
        mid2 = mid1 + (length - start) // 3
        print(arr, start, length, x)

        if arr[mid1] == x:
            return mid1

        if arr[mid2] == x:
            return mid2

        if arr[mid1] > x:
            return ternary_search(arr, start, mid1 - 1, x)

        if arr[mid2] < x:
            return ternary_search(arr, mid2 + 1, length, x)

    else:
        return -1


arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
x = 24
length = len(arr) - 1

result = ternary_search(arr, 0, length, x)
print(result)
