# This python script implement stack using stack
class Stack(object):

    def __init__(self):
        self.item = []

    # funtion to check if stack is empty
    def is_empty(self):
        return self.item == []

    # function to push/add value to stack
    def push(self, value):
        self.item.append(value)

    # function to remove value from stack. Since stack work on FILO it will remove value from end/tail
    def pop(self):
        return self.item.pop()

    # function to fetch last value of the stack. Fetches the last value (FILO)
    def peak(self):
        return self.item[len(self.item) - 1]

    # function to return the size of the stack
    def size(self):
        return len(self.item)


stack = Stack()
stack.size()
stack.push(1)
print(stack.size())
stack.push(2)
stack.push('three')
print(stack.pop())
print(stack.size())
print(stack.peak())
