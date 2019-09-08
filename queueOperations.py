queue = []

def enqueue(number):
    if(len(queue) == 0):
        print("There's no element in the queue. Adding first one: {0}".format(number))
        queue.append(number)
    else:
        queue.append(number)
        print("The new element in the queue is {0}".format(number))

def dequeue():
    if(len(queue) == 0):
        raise IndexError("There's no element in the queue. Add some!")
    else:
        print("Element out of the queue is:", queue.pop(0))

enqueue(2)
enqueue(4)
enqueue(7)
enqueue(9)
print(queue)
dequeue()
dequeue()
print(queue)