class CircularQueue:
    def __init__(self, size):
        # Declare size, front and rear
        self.size = size
        self.front = self.rear = -1
        # Declare items list to fixed size to understand the actual functionality of circular queue
        self.items = [None] *size

    # Insertion in queue is also known as Enqueue
    def enqueue(self, value):
        # If front and rear points the same index then circular queue is full
        if ((self.rear + 1) % self.size == self.front ):
            print("Queue is Full")
        # If front points -1 then queue is empty
        elif self.front == -1 :
            # Initialize front and rear to zero
            self.front = self.rear = 0
            # Insert value in items list at index zero. (rear and front points at first index zero)
            self.items[self.rear] = value
        else:
            # If values are already there in queue then check if rear follows the queue in clrcular by using this declared condition(size is 5 = if rear points 5 then with this condition it points to 0 to follow circular queue rule)
            self.rear = (self.rear + 1) % self.size
            # Insert at following index rear points
            self.items[self.rear] = value

    def dequeue(self):
        # Checks if queue is empty or not
        if (self.front == -1):
            print("Queue is empty")
        # If front and rear points same index then the queue has only one element left
        elif self.front == self.rear:
            print(self.items[self.front])
            # If no element means point front and rear to -1
            self.front = self.rear = -1
        else:
            print(self.items[self.front])
            # With this condition front follows circular queue flow
            self.front = (self.front + 1) % self.size

cq = CircularQueue(4)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()