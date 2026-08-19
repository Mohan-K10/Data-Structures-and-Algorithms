class Dequeue:
    # dequeue(double ended queue) is data structure where the insertion and deletion happens on both ends of queue
    def __init__(self):
        self.items = []

    # Checks if the queue is empty or not and returns boolean value
    def isEmpty(self):
        return len(self.items) == 0

    # Inserts at end by using append function. By default append adds element at last
    def insertAtEnd(self, value):
        self.items.append(value)

    # Deletes the last element by using pop(). By default pop deletes the last element
    def deleteAtEnd(self):
        if(self.isEmpty()):
            print("Dequeue is Empty")
        else:
            return self.items.pop()

    # Inserts the element at the first position of the queue. By using insert(), place the element at 0th index.
    def insertAtStart(self, value):
        self.items.insert(0, value)
        
    # Deletes the element at the first position of the queue. By using insert(), place the element at 0th index.
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
