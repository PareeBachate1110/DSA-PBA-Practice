class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def enqueue(self, x):
        newnode = Node(x)
        self.length += 1

        if self.front is None:
            self.front = newnode
            self.rear = newnode
        else:
            self.rear.next = newnode
            self.rear = newnode

    def dequeue(self):
        if self.front is None:
            return "Queue is Empty."

        self.length -= 1
        dq = self.front.data
        self.front = self.front.next

        if self.front is None:         #in case there was only one node which is now dequeued
            self.rear = None

        return "Dequeued : " + str(dq)

    def display(self):
        curr = self.front
        if self.front is None:
            return "Queue is Empty"

        result = "Queue: "

        while curr != None:
            result += str(curr.data)
            if curr.next != None:
                result += " "
            curr = curr.next
        return result

    def peek(self):
        if self.front == None:
            return "Queue is Empty"

        return "Front : " + str(self.front.data)


# Create queue
queue1 = Queue()

# Number of operations
n = int(input())

# Store outputs
output = []

for i in range(n):
    operation = input().split()

    if operation[0] == "ENQUEUE":
        number = int(operation[1])
        queue1.enqueue(number)
        output.append("Enqueued : " + str(number))

    elif operation[0] == "DISPLAY":
        output.append(queue1.display())

    elif operation[0] == "DEQUEUE":
        output.append(queue1.dequeue())

    elif operation[0] == "PEEK":
        output.append(queue1.peek())


# Print all outputs after reading all operations
for x in output:
    print(x)
