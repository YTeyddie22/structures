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
    
        
node1 = Node(3)
node2 = Node(5)
node3 = Node(15)
node4 = Node(1)

node1.next = node2
node2.next = node3
node3.next = node4

transverseAndPrint(node1)
print(findLowestVal(node1))


