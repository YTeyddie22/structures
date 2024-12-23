class Node:
    def __init__(self, data):
        self.data = data
        self.next = next
        
node1 = Node(2)
node2 = Node(13)
node3 = Node(5)
node4 = Node(10)


node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node1

currentNode = node1

#Check when the cycle is complete

startNode =  node1

print(currentNode.data,end="->")
currentNode = currentNode.next

while currentNode != startNode:
    print(currentNode.data, end="->")
    currentNode = currentNode.next
print("...")