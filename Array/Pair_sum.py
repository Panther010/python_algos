from nose.tools import assert_equal
# Python program to count sum pair of given number in a list

a1 = [1, 2, 3, 4, 5, 2]
n = 4


# function check and count the pairs of sum using set
def pair_sum1(arr, num):
    # Edge check if length of array is less than 2 than there wil not be any pair to achieve sum
    if len(arr) < 1:
        return

    # empty set for storing the number which is processed
    check = set()
    # Empty set for storing the result or pair sum
    result = set()

    # start looping array for numbers
    for num1 in arr:
        # check if number which will give use desired sum is present in set or not
        # if it is present add the pair to result set
        # if not add the number to processed set
        if num - num1 not in check:
            check.add(num1)
        else:
            result.add((min(num1, (num-num1)), max(num1, (num-num1))))

    print("\n".join(map(str, list(result))))

    return len(result)


print(pair_sum1(a1, n))

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""


class TestPair(object):

    def test(self, sol):
        assert_equal(sol([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10), 6)
        assert_equal(sol([1, 2, 3, 1], 3), 1)
        assert_equal(sol([1, 3, 2, 2], 4), 2)
        print('ALL TEST CASES PASSED')


# Run tests
t = TestPair()
t.test(pair_sum1)
