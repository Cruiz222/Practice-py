class Stack:
    def __init__(self):
        self.Stack_item = []

    def push(self, item):
        return self.Stack_item.append(item)

    def pop(self):
        return self.Stack_item.pop()

    def peek(self):
        return self.Stack_item[-1]

    def is_empty(self):
        return len(self.Stack_item) == 0

    def size(self):
        return len(self.Stack_item)            
