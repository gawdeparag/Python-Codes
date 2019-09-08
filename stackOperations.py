stack = []

def pushIntoStack(num):
    if(len(stack) == 0):
        print("Stack is empty! \nAdding first element: {0}".format(num))
        stack.append(num)
    else:
        stack.append(num)
        print("The new element at the top of the stack is {0}".format(num))

def popFromStack():
    if(len(stack) == 0):
        raise IndexError("Stack Underflow! Can't pop elements any further")
    else:
        print("The element popped from the stack is:", stack.pop())
    

pushIntoStack(2)
pushIntoStack(5)
pushIntoStack(6)
pushIntoStack(7)
print(stack)
popFromStack()
popFromStack()
popFromStack()
print(stack)
