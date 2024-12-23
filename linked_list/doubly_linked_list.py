class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
node1 = Node(3)
node2 = Node(15)
node3 = Node(1)
node4 = Node(10)


node1.next = node2
node2.prev = node1

node2.next = node3
node3.prev = node2

node3.next = node4
node4.prev = node3


currentNode = node1

print("\n Transversing from left")
while currentNode:
    print(currentNode.data,end="->")
    currentNode = currentNode.next
print("null")


currentNode = node4

print("\n Transversing from right")
while currentNode:
    print(currentNode.data,end="->")
    currentNode = currentNode.prev
print("null")


        