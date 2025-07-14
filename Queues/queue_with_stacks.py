from Stacks.stack import Stack

class Queue:
    def __init__(self):
        self._data = Stack()
        self._tempStack = Stack()

    def push(self, value): #O(1)
        self._data.push(value)

    def pop(self): #O(n)
        while self._data._data._head is not None:
            self._tempStack.push(self._data.pop())
        deletedValue = self._tempStack.pop()
        while self._tempStack._data._head is not None:
            self._data.push(self._tempStack.pop())
        self._tempStack = Stack()
        return deletedValue
    
    def traverse(self, functor):
       self._data._data.traverse(functor)
        