from collections import defaultdict
from nose.tools import assert_equal
# Python program to check and find out the missing element in an array
# after comparing it with another given array
a1 = [1, 2, 3, 4, 5, 6, 7]
a2 = [3, 7, 2, 1, 4, 6]


# method1 using inbuilt methods like sort and zip
def missing_element1(arr1, arr2):
    # sort both the array
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)

    # zip both the array and start comparing elements one by one
    # in case there is miss match we have got our missing element
    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1

    # in case zip method is not giving the result last element of array should be the missing element
    return arr1[-1]


# method 2 using default dictionary
# loop one array and add the count in the dictionary for each character
# start looping the second array by reducing the count
# in case count is 0 for one character we have got out character
def missing_element2(arr1, arr2):
    # empty default dictionary
    my_dict = defaultdict(int)

    # loop the second array with missing value and start adding the cunt is dictionary
    for i in arr2:
        my_dict[i] += 1

    # loop the first array by reducing the count in case count is zero we have got our element
    for num in arr1:
        if my_dict[num] == 0:
            return num
        else:
            my_dict[num] -= 1


# method 3 using XOR
def missing_element3(arr1, arr2):
    # create new array by adding both the array
    arr3 = arr1 + arr2
    result = 0

    # start looping and XOR at the end we will have out missing element only
    for k in arr3:
        result ^= k
    print(result)

    return result


print(missing_element1(a1, a2))
print(missing_element2(a1, a2))
print(missing_element3(a1, a2))

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""


class TestFinder(object):

    def test(self, sol, test):
        assert_equal(sol([5, 5, 7, 7], [5, 7, 7]), 5)
        assert_equal(sol([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]), 5)
        assert_equal(sol([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 5, 4, 3, 2, 1]), 6)
        print('ALL TEST CASES PASSED', test)


# Run test
t = TestFinder()
t.test(missing_element1, "test1")
t.test(missing_element2, "test2")
t.test(missing_element3, "test3")
