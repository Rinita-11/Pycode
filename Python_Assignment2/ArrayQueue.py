class Queue:
    def __init__(self):
        """Initialize an empty queue."""
        self.queue = []
    
    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.queue.append(item)
    
    def dequeue(self):
        """Remove and return the item from the front of the queue. Raise an exception if the queue is empty."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.queue.pop(0)
    
    def peek(self):
        """Return the item at the front of the queue without removing it. Raise an exception if the queue is empty."""
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.queue[0]
    
    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0
    
    def size(self):
        """Return the number of items in the queue."""
        return len(self.queue)
    
    def display(self):
        """Display all items in the queue."""
        print("Queue:", self.queue)
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.display()
print("Front element:", queue.peek())
print("Dequeued element:", queue.dequeue())
print("Dequeued element:", queue.dequeue())
queue.display()
print("Is queue empty?", queue.is_empty())
print("Size of queue:", queue.size())
