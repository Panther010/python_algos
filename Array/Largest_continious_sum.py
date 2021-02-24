from nose.tools import assert_equal
# Python program to check the largest continuous sum of numbers in a given array

a1 = [1, 2, -5, 3, 4, 10, 10, -10, -1]


# function to calculate and return the largest continuous sum of an array
def largest_sum(arr):
    # Edge check if length of array is 0
    if len(arr) == 0:
        return 0

    # assigning first value of array to largest sum to start
    large_sum = current_sum = arr[0]

    # starting with second value
    for i in arr[1:]:

        # check if previous sum is greater or current number
        # select either one is greater to ensure the sum will be largest from any position
        current_sum = max(current_sum+i, i)

        # check if sum after adding current number is greater then previous sum
        if large_sum < current_sum:
            large_sum = max(current_sum, large_sum)

    return large_sum


print(largest_sum(a1))
"""
RUN THIS CELL TO TEST THE SOLUTION
"""


class LargeContTest(object):

    def test(self, sol):
        assert_equal(sol([1, 2, -1, 3, 4, -1]), 9)
        assert_equal(sol([1, 2, -1, 3, 4, 10, 10, -10, -1]), 29)
        assert_equal(sol([-1, 1]), 1)
        print('ALL TEST CASES PASSED')


# Run Test
t = LargeContTest()
t.test(largest_sum)
