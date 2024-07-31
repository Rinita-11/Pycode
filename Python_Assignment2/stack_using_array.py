class Stack:
    def __init__(self):
        """Initialize an empty stack."""
        self.stack = []
    
    def push(self, item):
        """Push an item onto the stack."""
        self.stack.append(item)
    
    def pop(self):
        """Pop an item off the stack. Raise an exception if the stack is empty."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.stack.pop()
    
    def peek(self):
        """Return the top item of the stack without removing it. Raise an exception if the stack is empty."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.stack[-1]
    
    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0
    
    def size(self):
        """Return the number of items in the stack."""
        return len(self.stack)
    
    def display(self):
        """Display all items in the stack."""
        print("Stack:", self.stack)
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()
print("Top element:", stack.peek())
print("Popped element:", stack.pop())
print("Popped element:", stack.pop())
stack.display()
print("Is stack empty?", stack.is_empty())
print("Size of stack:", stack.size())
