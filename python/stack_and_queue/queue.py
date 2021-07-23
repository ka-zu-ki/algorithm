class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)
    
    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.queue)
q.dequeue()
print(q.queue)

from collections import deque

q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q)
q.popleft()
print(q)