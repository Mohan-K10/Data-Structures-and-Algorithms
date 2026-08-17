class Stack:
    def __init__(self):
        # Stack is stored in list format
        self.list = []

    def length(self):
        return len(self.list)

    def push(self, value):
        self.list.insert(0, value)

    def pop(self):
        if len(self.list) == 0:
            raise Exception("Stack is empty")
        else:
            return self.list.pop(0)

    def peek(self):
        if len(self.list) == 0:
            raise Exception("Stack is empty")
        else:
            return self.list[0]

stack = Stack()
stack.length
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.pop())
print(stack.pop())
print(stack.pop())
# print(stack.pop())
# print(stack.length())
        