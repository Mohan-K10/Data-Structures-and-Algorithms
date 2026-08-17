class Node:
    # Creates Node which contains data, prev and next 
    def __init__(self, value = None):
        self.data = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    # Head is assigned to Null when DLL calls
    def __init__(self):
        self.head = None

    # Insert Node at the end of DLL
    def insertAtEnd(self, value):
        # Store Node in temp
        temp = Node(value)
        # If there is no DLL then declare new Node as first Node of DLL and point head to new Node
        if self.head == None:
            self.head = temp
            return
        # If DLL exists then assign 't' and point it to first Node which is head
        t = self.head
        # Move 't' until it reaches last Node
        while t.next != None:
            t = t.next
        # Connect 't' with the temp Node
        t.next = temp
        temp.prev = t

    # Add Node at the beginning of DLL
    def insertAtBeg(self, value):
        # Store Node in temp 
        temp = Node(value)
        # If there is no DLL then declare the new Node as first Node and point head at this Node
        if self.head == None:
            self.head = temp
            return
        # If Nodes exist then connect the temp Node with the first Node of DLL and point head to this new Node and make it as first Node
        temp.next = self.head
        self.head.prev = temp
        self.head = temp

    # Insert Node at the middle of the node
    def insertAtMiddle(self, value, x):
        # Store new node in temp
        temp = Node(value)
        # Declare the var 't' and point it to the first Node and use it for traversal
        t = self.head
        # This loop works until var 't' reaches the last node
        while t.next != None:
            # Search the node which you want to find and add next to that node
            if t.data == x:
                # Connect new node(temp) with previous node and next node (t)
                temp.next = t.next
                t.next.prev = temp
                t.next = temp
                temp.prev = t
                break
            else:
                # Move the var 't' until data of node matches
                t = t.next

    # Delete the Node
    def deleteNode(self, value):
        # If no head exists then DLL is empty
        if self.head == None:
            print("Linked List is empty")

        # Declare 't' and point it to head and use it for traversal
        t = self.head
        # Deleting the first Node
        if t.data == value:
            self.head = t.next
            self.head.prev = None
            return
        # Deleting Middle Node
        while t.next != None:
            # If the Deleting Node Founds
            if t.data == value:
                # Connect the previous Node with the Next Node of Deleting Node, with this the Node have no connection and it automatically removes from memory
                t.prev.next = t.next
                t.next.prev = t.prev
                return 
            t = t.next
        # Deleting the last Node
        if t.data == value:
            t.prev.next = None

    # Print the Nodes 
    def printLL(self):
        t1 = self.head
        while t1.next != None:
            print(t1.data, end=" <--> ")
            t1 = t1.next
        print(t1.data)

obj = DoubleLinkedList()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtBeg(5)
obj.insertAtMiddle(70, 20)
obj.deleteNode(5)
obj.deleteNode(20)
obj.printLL()