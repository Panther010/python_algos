# Python3 program to implement
# interpolation search
# with recursion

def interpolation_search(arr, start, length, x):

    if (start <= length and x >= arr[start] and x <= arr[length]):
        position = start + ((length - start) *(x-arr[start]) //(arr[length]- arr[start]))
        print(arr, start, length, position, arr[position])
        if arr[position] == x:
            return position

        elif arr[position] < x:
            return interpolation_search(arr, position+1, length, x)

        else:
            return interpolation_search(arr, start, position-1,x)
    else:
        return -1


arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
x = 47
length = len(arr) -1
start = 0
result = interpolation_search(arr, start, length, x)
print(result)
