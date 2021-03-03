# Python script to implement queue using stack
class Queue2Stacks(object):

    def __init__(self):
        # two stack
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, value):
        self.in_stack.append()

    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()
