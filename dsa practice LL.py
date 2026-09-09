class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, number):       #(at end)
        newnode = Node(number)

        if self.head is None:       #if head is not pointing to anything i.e. LL has no nodes right now
            self.head=newnode       #make newnode as the head
            return
                                    
        curr=self.head              #else make head node the curr node
        while curr.next!=None:      #until curr reaches None
            curr=curr.next          #keep going to the next node
        curr.next=newnode           #at the next pointer of current node (i.e the last node), join newnode

    def delete(self):                   #(at end)
        if self.head is None:           #if there are currently no nodes
            return "List is Empty"      
            

        if self.head.next is None:                  #special case where LL has only one node
            deleted = self.head.data                #store value to be deleted so we can print it
            self.head=None                          #set head to none, hence the LL is empty now
            return "Deleted : " + str(deleted)
            
        curr=self.head                              #else make head node the curr node

        while curr.next.next!=None:                 #since last node is curr.next, penultimate node will be curr.next.next
            curr=curr.next                          #keep traversing while true

        deleted = curr.next.data                    #store value to be deleted so we can print it
        curr.next=None                              #point next of penultimate node to None so that the last node will exit
        return "Deleted : " + str(deleted)        
       
    def display(self):
        if self.head is None:
            return "List is empty"

        curr = self.head
        result = "List: "
        while curr != None:
            result += str(curr.data)

            if curr.next != None:
                result += " "
            curr = curr.next
        return result



# Create linked list
list1 = LinkedList()

# Number of operations
n = int(input())

# Store outputs
output = []

for i in range(n):
    operation = input().split()

    if operation[0] == "INSERT":
        number = int(operation[1])
        list1.insert(number)
        output.append("Inserted: " + str(number))


    elif operation[0] == "DISPLAY":
        output.append(list1.display())

    elif operation[0] == "DELETE":
        output.append(list1.delete())

for x in output:
    print(x)