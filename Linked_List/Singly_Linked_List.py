# Python script to implement singly linked list
class LinkedList(object):

    def __init__(self, value):
        self.value = value
        self.nextnode = None


a = LinkedList(1)
b = LinkedList(2)
c = LinkedList(3)

a.nextnode(b)
b.nextnode(c)
