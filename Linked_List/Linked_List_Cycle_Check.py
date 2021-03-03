# Python script to check if linked list is cyclic or not
from nose.tools import assert_equal
class Node(object):

    def __init__(self, value):
        self.value = value
        self.next_node = None


a = Node(1)
b = Node(2)
c = Node(3)

a.next_node = b
b.next_node = c
c.next_node = a  # Cycle Here!

# CREATE NON CYCLE LIST
x = Node(1)
y = Node(2)
z = Node(3)

x.next_node = y
y.next_node = z


def cyclic_check(node):

    maker1 = node
    maker2 = node
    # print(maker1, maker2)

    while maker2 is not None and maker2.next_node is not None:

        maker1 = maker1.next_node
        maker2 = maker2.next_node.next_node
        # print(maker1.next_node, maker2)

        if maker1 == maker2:
            return True

    return False

print(cyclic_check(x))
"""
RUN THIS CELL TO TEST YOUR SOLUTION

"""
# CREATE CYCLE LIST


#############
class TestCycleCheck(object):

    def test(self, sol):
        assert_equal(sol(a), True)
        assert_equal(sol(x), False)

        print("ALL TEST CASES PASSED")


# Run Tests

t = TestCycleCheck()
t.test(cyclic_check)

