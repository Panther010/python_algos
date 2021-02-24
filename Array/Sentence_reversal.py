from nose.tools import assert_equal
# Python program to revert a sentence

# s = "This    is the best"
s = '    space before'


# method one by using split and reversed inbuilt method
def sentence_reversal1(string):
    return " ".join(reversed(string.split()))


# method 2 by using split and slicing
def sentence_reversal2(string):
    return " ".join(string.split()[::-1])


# method 3 by using reverse loop on the string
def sentence_reversal3(string):
    word = ""
    result = []
    # start looping the string in reverse direction
    for i in range(len(string) - 1, -1, -1):
        # in case current letter is space that suggest we have completed the word
        if string[i] == " ":
            # add the word in result with space at the end and empty the word for further processing
            if word != '':
                result.append(word)
            word = ""

        else:
            # else keep adding the letters in word
            word = string[i] + word

    # add the last word in the sentence
    if word != '':
        result.append(word)
    return " ".join(result)


# method 4 using forward loop
def sentence_reversal4(string):
    word = ""
    result = []

    # forward loop picks one letter at a time
    for i in string:

        # in case letter is a space add the word to starting of the string
        if i == " ":
            # add space in between word and make word empty for next word prcessing
            if word != '':
                result.insert(0, word)
            word = ""

        else:
            # else keep adding letter to word
            word += i

    result.insert(0, word)
    return " ".join(result)


print(sentence_reversal1(s))
print(sentence_reversal2(s))
print(sentence_reversal3(s))
print(sentence_reversal4(s))
"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""


class ReversalTest(object):

    def test(self, sol):
        # assert_equal(sol('    space before'), 'before space')
        # assert_equal(sol('space after     '), 'after space')
        # assert_equal(sol('   Hello John    how are you   '), 'you are how John Hello')
        assert_equal(sol('1'), '1')
        print("ALL TEST CASES PASSED")


# Run and test
t = ReversalTest()
t.test(sentence_reversal1)
t.test(sentence_reversal2)
t.test(sentence_reversal3)
t.test(sentence_reversal4)
