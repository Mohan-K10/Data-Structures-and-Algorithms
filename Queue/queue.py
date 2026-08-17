class Queue:
    # Queue is a data structure that follows FIFO (First In First Out).  
    def __init__(self):
        self.queue = []
    # Checks if Queue is Empty or Not
    def isEmpty(self):
        return len(self.queue) == 0
    
    # Insert element in Queue
    # It avoids front and rear to track values(which is used in c, cpp) but in python append automatically adds element at last
    # Front and rear is used to check if the queue is underflow or overflow. 
    def insert(self, value):
        self.queue.append(value)

    # Delete element in Queue
    def delete(self):
        if(self.isEmpty()):
            print("The Queue is Empty")
        else:
            return self.queue.pop(0)


q = Queue()
q.insert(10)
q.insert(20)
q.insert(30)
print(q.delete())
print(q.delete())
print(q.delete())
