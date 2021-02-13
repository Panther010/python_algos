# Python program for implementation of Bubble Sort

def bubble_sort(arr):
    length = len(arr)

    for i in range(length):

        for j in range(0, length - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(arr)

    return arr


a = [64, 34, 25, 90, 22, 11, 12]
print(a)
result = bubble_sort(a)
print(result)
