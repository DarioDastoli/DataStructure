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
            self._head = SinglyLinkedList.Node(data)
        else:
            while current.next() is not None:
                current = current.next()
            current.append(SinglyLinkedList.Node(data))
    
    def insert_in_front(self, data):
        old_head = self._head
        self._head = SinglyLinkedList.Node(data, old_head)

    def traverse(self, functor):
        current = self._head
        result = []
        while current is not None:
            result.append(functor(current.data()))
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
                
    def delete_from_front(self):
        if self._head is None:
            raise ValueError('Delete on an empty list')
        data = self._head.data()
        self._head = self._head.next()
        return data
    
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




