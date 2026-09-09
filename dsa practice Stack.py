class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.top=None
        self.length=0

    def push(self,x):               #insert (at beginning)
        self.length+=1

        if self.top is None:        #if stack is empty
            self.top=Node(x)        #create new node and set it to top
            return
        
        else:
            newnode=Node(x)             #create new node
            newnode.next=self.top       #set next pointer of newnode to current top
            self.top=newnode            #set newnode as top
        
    def pop(self):                      #delete (at beginning)
        if self.top == None:
            return "Stack is Empty"
        
        self.length-=1
        popped=self.top.data            #store top
        self.top=self.top.next          #set next node at top

        return "Popped :" + str(popped)

    def peek(self):
        if self.top == None:
            return "Stack is Empty"
        
        return "Top : " + str(self.top.data)
        

    def display(self):
        curr = self.top                     #start at top

        if self.top is None:
            return "Stack is empty"

        result = "Stack: "

        while curr != None:                 #until curr is None
            result += str(curr.data)        #store current data in result
            if curr.next != None:           #if theres another node present after curr
                result += " "               #separate with space
            curr = curr.next                #traverse
        return result

# Create stack
stack1 = Stack()

# Number of operations
n = int(input())

# Store outputs
output = []

for i in range(n):
    operation = input().split()

    if operation[0] == "PUSH":
        number = int(operation[1])
        stack1.push(number)
        output.append("Pushed : " + str(number))

    elif operation[0] == "DISPLAY":
        output.append(stack1.display())

    elif operation[0] == "POP":
        output.append(stack1.pop())

    elif operation[0] == "PEEK":
        output.append(stack1.peek())

# Print all outputs after reading all operations
for x in output:
    print(x)