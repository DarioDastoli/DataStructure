class SinglyLinkedList():
    
    class Node:
        def __init__(self, data, next_node = None):
            self._data = data
            self._next = next_node

        def data(self):
            return self._data
        
        def next(self):
            return self._next
        
        def has_next(self):
            self.next is not None

        def append(self, next_node):
            self._next = next_node

    def __init__(self):
        self._head = None

    def insert(self, data):
        old_head = self._head
        self._head = SinglyLinkedList.Node(data, old_head)
        
    def search(self, target):
        current = self._head
        while current is not None:
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


    def delete_from_front(self) -> any:
        if self.is_empty():
            raise ValueError('List is empty')
        data = self._head.data
        self._head = self._head.next()
        return data
    
    def traverse(self, functor: callable[..., any]):
        current = self._head
        result = []
        while current is not None:
            result.append(functor(current.data))
            current = current.next()
        return result


