# Python3 Program for jump search.
# Returns index of x in arr if present, else -1
import math

def jump_search(arr, x, length):
    step = int(math.sqrt(length))

    prev = 0
    while arr[min(step, length) - 1] < x:
        #print(step-1, arr)
        prev = step
        step += int(math.sqrt(length))
        if prev >= length:
            return -1

    for i in range(prev, step):
        if i <= length:
            if arr[i] == x:
                return i
    return -1


#arr = [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 700]
arr = [ 0, 1, 1, 2, 3, 5, 8, 13]
x = 3
length = len(arr)

result = jump_search(arr, x, length)
print(result)