class Node:
    # Node consists of data and address of next node. By default next value is assigned as None
    def __init__(self, value, next = None):
        self.data = value
        self.next = next

class SinglyLinkedList:
    # Head pointer is assigned to Node
    def __init__(self, head = None):
        self.head = head

    # Insert Node at End of LL
    def insertAtEnd(self, value):
        # store the value of Node in temp
        temp = Node(value)
        # If Nodes already exists
        if self.head != None:
            # Assign the dummy pointer t1 to head and move it until it reaches Last Node
            t1 = self.head
            while t1.next != None:
                t1 = t1.next
            # Attach the temp which contains the new Node to last Node
            t1.next = temp
        else:
            # If no LL then assign the temp to head and make it as first Node of LL
            self.head = temp

    # Insert Node at the Beginning of LL
    def insertAtBeg(self, value):
        # Assign temp for New Node
        temp = Node(value)
        # Connect temp to the first Node(which contains head)
        temp.next = self.head
        # Point head to the New Node which makes it as the First Node of LL
        self.head = temp

    def InsertAtMid(self, value, x):
        temp = Node(value)
        t1 = self.head
        while t1.next != None:
            if t1.data == x:
                temp.next = t1.next
                t1.next = temp
            t1 = t1.next

    def deleteNode(self, value):
        # Declare t1 and prev in first Node(head)
        t1 = self.head
        prev = t1

        # To delete First Node
        if t1.data == value:
            # Shift the head pointer to next Node with help of t1
            self.head = t1.next

        # To delete one of the Middle Nodes
        while t1.next != None:
            # Find the location of that particular Node
            if t1.data == value:
                # Remove it by pointing prev node to the next address of the current node
                prev.next = t1.next
                break
            else:
                # prev node always points to the previous node of t1 pointer
                prev = t1
                t1 = t1.next
        # Delete Last Node
        if t1.data == value:
            # Declare prev next address as Null
            prev.next = None
            

    # Print the Nodes
    def printLL(self):
        # Declare T1 pointer and use it to print all Values. Declare t1 to head (first Node)
        t1 = self.head
        # Move the t1 until it reaches the Node before last Node
        while t1.next != None:
            # In this process of moving t1 print the Node data when t1 iterates through Node
            print(t1.data, end=" --> ")
            t1 = t1.next
        # Print the Last Node data
        print(t1.data)

# create an object 'obj' for singlyLinkedList
obj = SinglyLinkedList()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.InsertAtMid(50, 20)
obj.deleteNode(30)
obj.deleteNode(50)
obj.printLL()