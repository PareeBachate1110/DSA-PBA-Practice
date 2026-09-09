class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length=0

    def enqueue(self,x):
        newnode=Node(x)
        print("Enqueued :",x)
        self.length+=1
        if self.front is None:
            self.front=newnode
            self.rear=newnode
        else:
            self.rear.next=newnode
            self.rear=newnode

    def dequeue(self):
        if self.front is None:          #if initially empty
            print("Queue is Empty.")
            return

        self.length-=1
        dq=self.front.data
        self.front=self.front.next
        print("Dequeued :",dq)

        if self.front is None:          #after everything is dequeued
            self.rear = None
            return
        

    def display(self):
        curr = self.front

        if self.front is None:
            print("Queue is Empty")
            return
        else:
            while curr != None:
                print(curr.data, end=" ")
                curr = curr.next
                return
        print()

    def peek(self):
        if self.front == None:
            print("Queue is Empty")
        else:
            print("Front :",self.front.data)

# Create queue
queue1 = Queue()

# Number of operations
n = int(input())

for i in range(n):
    operation = input().split()

    if operation[0] == "ENQUEUE":
        number = int(operation[1])
        queue1.enqueue(number)

    elif operation[0] == "DISPLAY":
        queue1.display()

    elif operation[0] == "DEQUEUE":
        queue1.dequeue()

    elif operation[0] == "PEEK":
        queue1.peek()
    
