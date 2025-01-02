class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Transversal
def transverseAndPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data,end="-> ")
        currentNode = currentNode.next
    print("null")
    
# Finding the lowest value

def findLowestVal(head):
    minValue = head.data
    currentNode = head.next
    while currentNode:
        if currentNode.data < minValue:
            minValue = currentNode.data
        currentNode = currentNode.next
    return minValue

# Deleting node from linked list

def deleteNode(head, deletedNode):
    if head == deletedNode:
        return head.next
    
    currentNode = head
    
    while currentNode.next and currentNode.next != deletedNode:
        currentNode = currentNode.next 
        
    if currentNode.next == None:
        return head
    
    currentNode.next = currentNode.next.next 
    
    return head
    
# Insert a New node

def insertNode(head, newNode, position):
    if position == 1:
        newNode.next = head
        return newNode
    
    currentNode = head
    
    for _ in range(position - 2):
        if currentNode is None:
            break
        currentNode = currentNode.next

    newNode.next = currentNode.next 
    currentNode.next = newNode
    
    return head

       
node1 = Node(3)
node2 = Node(5)
node3 = Node(15)
node4 = Node(1)

node1.next = node2
node2.next = node3
node3.next = node4

print("Original Node List")
transverseAndPrint(node1)
print("Lowest value")
print(findLowestVal(node1))
node1 = deleteNode(node1, node4)
print("Nodes after deleting a node")
transverseAndPrint(node1)

newNode = Node(66)
node1 = insertNode(node1, newNode, 4)
print("Node list after inserting")
transverseAndPrint(node1)




