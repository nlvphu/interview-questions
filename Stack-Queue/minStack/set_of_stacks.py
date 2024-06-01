from stack import Stack

class SetOfStacks:
    def __init__(self):
        self.stacks = [Stack()]

    def push(self, item):
        last = self.getLastStack()

        if last != None and not last.isFull():
            last.push(item)    
        else:   
            stack = Stack()
            stack.push(item)
            self.stacks.append(stack)
    
    def pop(self):
        last = self.getLastStack()

        if last == None:
            raise IndexError("pop from empty stack list")
        
        v = last.pop()
        if last.is_empty():
            self.stacks.pop()
        return v

    def getLastStack(self):
        return self.stacks[-1]   