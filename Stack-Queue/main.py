from stack_min import *
from set_of_stacks import *        

# Example usage:
if __name__ == "__main__":
    # stack = Stack()
    # stack.push(1)
    # stack.push(2)
    # stack.push(3)

    # print("Stack size:", stack.size())  # Output: Stack size: 3
    # print("Top element:", stack.peek())  # Output: Top element: 3
    # print("Popped element:", stack.pop())  # Output: Popped element: 3
    # print("Stack is empty:", stack.is_empty())  # Output: Stack is empty: False


    # stack_1 = StackMin()
    # stack_1.push(2)
    # stack_1.push(5)
    # stack_1.push(7)
    # stack_1.push(1)

    # print("Stack size:", stack_1.size())  # Output: Stack size: 3
    # print("Top element:", stack_1.peek())  # Output: Top element: 3
    # print("Popped element:", stack_1.pop())  # Output: Popped element: 3
    # print("Min element: ", stack_1.minimum()) 
    # print("Stack is empty:", stack_1.is_empty())  # Output: Stack is empty: False

    setStack = SetOfStacks()
    for i in range(10):
        setStack.push(i)

    print(setStack.pop())
    print(setStack.pop())
