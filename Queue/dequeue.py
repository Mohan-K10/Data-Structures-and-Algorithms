class Dequeue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def insertAtEnd(self, value):
        self.items.append(value)

    def deleteAtEnd(self):
        if(self.isEmpty()):
            print("Dequeue is Empty")
        else:
            return self.items.pop()

    def insertAtStart(self, value):
        self.items.insert(0, value)

    def deleteAtFront(self):
        if(self.isEmpty()):
            print("Dequeue is Empty")
        else: 
            return self.items.pop(0)

dq = Dequeue()
dq.insertAtStart(10)
dq.insertAtStart(20)
dq.insertAtEnd(80)
dq.insertAtEnd(90)
print(dq.deleteAtFront())
print(dq.deleteAtFront())
print(dq.deleteAtEnd())
print(dq.deleteAtEnd())
print(dq.deleteAtEnd())
