# Python program for implementation of Insertion Sort


def insertion_sort(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        print(arr)

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            print("while***** ", arr)
        arr[j+1] = key

    return arr


a = [64, 34, 25, 90, 22, 11, 12]
print(a)
result = insertion_sort(a)
print(result)
