# This python script implement deque using list
class Deque(object):

    def __init__(self):
        self.item = []

    # function to check if the deque is empty
    def is_empty(self):
        return self.item == []

    # function to add element at front in deque
    def add_front(self, value):
        self.item.insert(0, value)

    # function to add element at the rear of deque
    def add_rear(self, value):
        self.item.append(value)

    # function to remove element from the from of the deque
    def remove_front(self):
        return self.item.pop(0)

    # function to remove element from the back of the deque
    def remove_rear(self):
        return self.item.pop()

    # function to return the size of the deque
    def size(self):
        return len(self.item)


deq = Deque()
print(deq.size())
deq.add_front(2)
deq.add_front(1)
deq.add_rear(3)
print(deq.remove_front())
print(deq.remove_rear())
print(deq.remove_rear())
print(deq.is_empty())
