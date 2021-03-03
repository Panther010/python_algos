# Python script to implement doubly linked list
class DoublyLinkedList(object):

    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.previous_node = None


a = DoublyLinkedList(1)
b = DoublyLinkedList(2)
c = DoublyLinkedList(3)

a.next_node = b
b.previous_node = a

c.previous_node = b
b.next_node = c
