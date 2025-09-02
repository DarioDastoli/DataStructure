from Stacks.stack import Stack

"""EXERCISE
    9.1 As mentioned, it is also possible to use stacks to store a queue's data. One stack, however,
        is not enough. 
        Can you find a way to use two stacks to implement a queue?
        Hint: Either enqueue or dequeue will have to be O(n).
"""

class Queue:
    def __init__(self):
        self._data = Stack()
        self._tempStack = Stack()

    def push(self, value): #O(1)
        self._data.push(value)

    def pop(self): #O(n)
        while not self._data.is_empty():
            self._tempStack.push(self._data.pop())
        deletedValue = self._tempStack.pop()
        while not self._tempStack.is_empty():
            self._data.push(self._tempStack.pop())
        self._tempStack = Stack()
        return deletedValue
    
    def traverse(self, functor):
       self._data._data.traverse(functor)
        