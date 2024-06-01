from stack import *

#implement queue with 2 stacks

# In this approach, stackNewest has the newest elements on top and stackOldest has the oldest
# elements on top. When we dequeue an element, we want to remove the oldest element first, and so we
# dequeue from stackOldest. If stackOldest is empty, then we want to transfer all elements from
# stackNewest into this stack in reverse order. To insert an element, we push onto stackNewest, since it
# has the newest elements on top.

class MyQueue:
    def __init__(self):
        self.StackNewest = Stack()
        self.StackOldest = Stack()

    def size(self):
        return self.StackNewest.size() + self.StackOldest.size()
    
    def enqueue(self, item):
        #add value into the newest
        self.StackNewest.push(item)

    
    def shiftStacks(self):
        if self.StackOldest.is_empty():
            while not self.StackNewest.is_empty():
                self.StackOldest.push(self.StackNewest.pop())
    
    def dequeue(self):
        self.shiftStacks()
        self.StackOldest.pop()
       