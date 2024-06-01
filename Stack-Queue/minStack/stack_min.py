from stack import Stack

import sys

class NodeWithMin:
    def __init__(self, value, minimum):
        self.value = value
        self.min = minimum
    

class StackMin(Stack):
    def push(self, item):
        newMin = min(item, self.minimum())
        super().push(NodeWithMin(item, newMin))
        

    def minimum(self):
        if self.is_empty():
            return sys.maxsize
        else:
            return self.items[-1].min
    
    def peek(self):
        return super().peek().min

    def pop(self):
        return super().pop().value