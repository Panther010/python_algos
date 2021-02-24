from nose.tools import assert_equal
# python program to compress the string
s = "AAAABBBBCCCCCDDEEEE"


# function to compress string
def string_compression(string):

    count = 1
    result = ""

    # edge check if length of  given string is 0
    if len(string) == 0:
        return ""

    # edge check if length of given string is 1
    if len(string) == 1:
        return string + "1"

    # first letter assignment
    previous_letter = string[0]

    # start looping the string from second character
    for i in range(1, len(string)):
        # if current letter is same as previous letter increase the count
        if string[i] == previous_letter:
            count += 1
        else:
            # else add the letter and the count to result string
            # move current letter to previous letter
            result += previous_letter + str(count)
            previous_letter = string[i]
            count = 1

    result += previous_letter + str(count)

    return result


print(string_compression(s))
"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""


class TestCompress(object):

    def test(self, sol):
        assert_equal(sol(''), '')
        assert_equal(sol('AABBCC'), 'A2B2C2')
        assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
        print('ALL TEST CASES PASSED')


# Run Tests
t = TestCompress()
t.test(string_compression)
