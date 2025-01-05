class Node:
    def __init__(self, value):
        self.value = value
        self.next = None 
        
class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def isEmpty(self):
        return self.size == 0
    
    def stackSize(self):
        return self.size
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        
        return self.head.value
        
    def push(self, value):
        new_node = Node(value)
        
        if self.head:
            new_node.next = self.head
            
        self.head = new_node
        self.size += 1
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        
        removed_node = self.head
        self.size -= 1
        self.head = self.head.next 
        return removed_node.value
    

myStack = Stack()
myStack.push('A')
myStack.push('B')
myStack.push('C')

print("Pop: ", myStack.pop())
print("Peek: ", myStack.peek())
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.stackSize())
        
        