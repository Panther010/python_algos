from nose.tools import assert_equal
# python program to check if string contains all the unique character
s = "goo"


# method 1 to convert string into set and compare length of string and set
def unique_char1(string):
    return len(set(string)) == len(string)


# method 2 loop through string, check if string is present in set if yes then character is repetitive return False
# else add it in the set
def unique_char2(string):
    check = set()
    for i in string:
        if i in check:
            return False
        else:
            check.add(i)

    return True


print(unique_char1(s))
print(unique_char2(s))
"""
RUN THIS CELL TO TEST YOUR CODE>
"""


class TestUnique(object):

    def test(self, sol):
        assert_equal(sol(''), True)
        assert_equal(sol('goo'), False)
        assert_equal(sol('abcdefg'), True)
        print('ALL TEST CASES PASSED')


# Run Tests
t = TestUnique()
t.test(unique_char1)
t.test(unique_char2)
