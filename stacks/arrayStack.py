class Stack:
    def __init__(self):
        self.stack = []
        
    def isEmpty(self):
        return len(self.stack) == 0
        
    # Adding elements
    def push(self, element):
        self.stack.append(element)
    
    # Removing elements
    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
        self.stack.pop()
        
    def size(self):
        return len(self.stack)
    
    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
        return self.stack[-1]
   

# Create a stack
myStack = Stack()

myStack.push('A')
myStack.push('B')
myStack.push('C')
print("Stack: ", myStack.stack)

print("Pop: ", myStack.pop())

print("Peek: ", myStack.peek())

print("isEmpty: ", myStack.isEmpty())

print("Size: ", myStack.size()) 
    
        
    