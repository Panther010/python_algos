# Python program to check if the passed parentheses sting is balanced or not
def balance_check(s):
    # edge check if the passed string is of odd length it will not be balanced
    if len(s)%2 != 0:
        return False

    # set of open parentheses and combination
    open_paren = set('({[')
    match_pair = set([('(', ')'), ('{', '}'), ('[', ']')])

    # empty stack using list
    stack = []

    # looping through string from left to right
    for paren in s:
        # in case parentheses is present in open set add it to stack
        if paren in open_paren:
            stack.append(paren)
        else:
            # else fisrt check length of stack should not be 0 to match with its open parentheses
            if len(stack) == 0:
                return False

            # fetch the last open parentheses. it should match with the close
            last_open = stack.pop()

            # make the tuple of last open and current close parentheses. it should be present in match set
            if(last_open, paren) not in match_pair:
                return False

    # at end length of stack should be zero for balance
    return len(stack) == 0


print(balance_check('[]'))
print(balance_check('[](){([[[]]])}'))
print(balance_check('()(){]}'))
