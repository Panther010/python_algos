# this python program implement queue using list
class Queue(object):

    def __init__(self):
        self.item = []

    # function to check if the queue is empty
    def is_empty(self):
        return self.item == []

    # function to add value to the queue
    def enqueue(self, value):
        self.item.append(value)

    # function to remove item from the queue. It wil remove item from front since it works on FIFO
    def dequeue(self):
        return self.item.pop(0)

    # funtion to fetch the size of the queue
    def size(self):
        return len(self.item)


q = Queue()
print(q.is_empty())
q.enqueue(1)
q.enqueue('two')
q.enqueue(3)
print(q.size())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.is_empty())
