# Python program for implementation of Selection
# Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            #print(i, j, arr[i], arr[j])
            if arr[min_index] > arr[j]:
                min_index = j

        arr[i],  arr[min_index] = arr[min_index], arr[i]
        #print(i, arr)

    return arr


a = [64, 25, 12, 22, 11]
print(a)
result = selection_sort(a)
print(result)
