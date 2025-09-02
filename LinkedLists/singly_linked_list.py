class SinglyLinkedList:

    class Node:
        def __init__(self, data, next_node = None):
            self._data = data
            self._next = next_node

        def data(self):
            return self._data
        
        def next(self):
            return self._next
        
        def has_next(self):
            return self._next is not None
        
        def append(self, next_node):
            self._next = next_node

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def insert_to_back(self, data):
        current = self._head
        if current is None:
            self._head = self.Node(data)
        else:
            while current.next() is not None:
                current = current.next()
            current.append(self.Node(data))
    
    def insert_in_front(self, data):
        old_head = self._head
        self._head = self.Node(data, old_head)

    """
        6.2 Implement the traverse method for singly linked lists. The method should take a
            function that can be applied to the data stored in the list and return a Python list
            with the result of applying such a function.
    """
    def traverse(self, callback):
        current = self._head
        result = []
        # Cannot use has_next or last element will be skipped
        while current is not None:
            result.append(callback(current.data()))
            current = current.next()
        return result

    def search(self, target):
        current = self._head
        while current.next() is not None:
            if current.data() == target:
                return current
            current = current.next()
        return None
    
    def delete(self, target):
        current = self._head
        previous = None
        while current is not None:
            if current.data() == target:
                if previous is None:
                    self._head = current.next() 
                else:
                    previous.append(current.next())
                return
            previous = current
            current = current.next()
        raise ValueError(f'No element with value {target} was found in the list')
                
    """
        EXERCISES
        6.1 Implement a delete_from_front method that removes and returns the head of
            the list. Hint: This is an edge case in the general-purpose delete method.
    """
    def delete_from_front(self):
        if self._head is None:
            raise ValueError('Delete on an empty list')
        data = self._head.data()
        self._head = self._head.next()
        return data
    
    """
    EXERCISES
    8.1 Implement a get(i) method for linked lists that returns the i-th element from the
        head of the list (i≥0). Then, modify the implementation of peek to avoid accessing
        the _head private attribute of the linked list.
    """
    
    def get(self, index):
        if index < 0:
            raise IndexError("Index must be non-negative")
        i = 0
        current = self._head
        while i < index and current is not None:
            current = current.next()
            i += 1
        if current is None:
            raise IndexError("Index out of bounds")
        return current.data()
    

    """
    EXERCISE
    8.4 Write a method that reverses an SLL. 
        Hint: How can you use a stack to perform the task? 
        What would be the running time of the operation?  -> O(n)
    """
    def reverse_list(self) -> 'SinglyLinkedList':
        from Stacks.stack import Stack
        current = self._head
        reversed_elements = Stack()
        result = SinglyLinkedList()
        while current is not None: #O(N)
            reversed_elements.Push(current.data()) #O(1)
            current = current.next()
        while not reversed_elements.is_empty(): #O(N)
            try:
                value = reversed_elements.Peek() #O(1)
                reversed_elements.Pop() #O(1)
                result.insert_in_front(value) #O(1)
            except Exception as e:
                raise
        return result

