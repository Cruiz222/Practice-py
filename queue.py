from collections import deque

class Queue:
    def __init__(self):
        self.deque = deque()

    def enqueue(self, item):
        return self.deque.appendright(ime)

    def dequeue(self):
        if len(self.deque) == 0:
            raise ValueError("Queue is empty")

        return self.deque.popleft()     

    def peek(self):
        return self.deque[0]

    def is_empty(self) -> bool:
        return len(self.deque) == 0

    def size(self) -> int:
        return len(self.deque)