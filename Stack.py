
class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        pass

    def pop(self):
        pass

    def peek(self):
        if self.head is None:
            return "The stack is empty"
        else:
            return self.head.data


Test = Stack()

