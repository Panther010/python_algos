from nose.tools import assert_equal
from collections import Counter
# Python program and logic to check if two given string are Anagram.
# Two strings are called anagram once they have exactly similar character
# characters might be shuffled

s1 = "my name"
s2 = "name my"


# approach 1 using default sort method of python
def anagram_check1(str1, str2):
    # ignore spaces in the string and convert complete string to lower case
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    # sort and compare the string
    return sorted(str1) == sorted(str2)


# approach 2 using dictionary default sorted method will not be used
def anagram_check2(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Edge case where if length of both the string is not same by default these wil not be anagram
    if len(str1) != len(str2):
        return False

    # dictionary for counting the letters and occurrence
    check = {}

    # loop the string one letter by letter in case letter if present increase the count
    # else add the letter with count one
    for letter in str1:
        if letter in check:
            check[letter] += 1
        else:
            check[letter] = 1

    # loop the second string and start reducing the count
    for letter in str2:
        if letter in check:
            check[letter] -= 1
        else:
            return False

    # loop to check if all the character's matched
    for key in check:
        if check[key] != 0:
            return False

    return True


# approach 3 using collections, counters
def anagram_check3(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    check = Counter(str1)

    for letter in str2:
        if letter in check:
            check[letter] -= 1
        else:
            return False

    for key in check:
        if check[key] != 0:
            return False

    return True


print(anagram_check3(s1, s2))
"""
RUN THIS CELL TO TEST THE SOLUTION
"""


class AnagramTest(object):

    def test(self, sol, func_name):
        assert_equal(sol('go go go', 'gggooo'), True)
        assert_equal(sol('abc', 'cba'), True)
        assert_equal(sol('hi man', 'hi     man'), True)
        assert_equal(sol('aabbcc', 'aabbc'), False)
        assert_equal(sol('123', '1 2'), False)
        print("ALL TEST CASES PASSED in", func_name)


# Run Tests
t = AnagramTest()
t.test(anagram_check1, "check1")
t.test(anagram_check2, "check2")
t.test(anagram_check3, "check3")
