class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.stack:
            return self.stack.pop()

stack = Stack()
print(stack.stack)
stack.push(1)
stack.push(2)
print(stack.stack)
stack.pop()
print(stack.stack)