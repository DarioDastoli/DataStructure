class DoubleLinkedList:

    def __init__(self):
        self._head = None
        self._tail = None
    
    class Node:

        def __init__(self, data):
            self._data = data
            self._next = None
            self._previous = None

        def data(self):
            return self._data
        
        def next(self):
            return self._next
        
        def previous(self):
            return self._previous
        
        def has_next(self) -> bool:
            return self.next() is not None
        
        def has_previous(self) -> bool:
            return self._previous is not None
        
        def append(self, next_node):
            self._next = next_node
            if next_node is not None:
                next_node._previous = self

        def prepend(self, prev_node):
            self._previous = prev_node
            if prev_node is not None:
                prev_node._next = self

    def insert_in_front(self, data):
        if self._head is None:
            self._tail = self._head = DoubleLinkedList.Node(data)
        else:
            old_head = self._head
            self._head = DoubleLinkedList.Node(data)
            self._head.append(old_head)

    def insert_at_back(self, data):
        if self._tail is None:
            self._tail =  self._head = DoubleLinkedList.Node(data)
        else:
            old_tail = self._tail
            self._tail = DoubleLinkedList.Node(data)
            self._tail.prepend(old_tail)

    def is_empty(self) -> bool:
        return self.Node.has_next()
    
    def delete_from_front(self) -> Node.data:
        if self._head is None:
            raise ValueError('Delete on an empty list')
        data = self._head.data()
        self._head = self._head.next()
        return data
    
    def delete_from_back(self):
        if self._tail is None:
            raise ValueError('Delete on an empty list')
        data = self._tail.data()
        if self._tail._previous is not None:
            self._tail = self._tail._previous
            self._tail._next = None
        else:
            self._head = self._tail = None
        return data
    
    def delete(self, target):
        current = self._head
        previous_node = None
        while current is not None:
            if current.data() == target:
                if previous_node is None:
                    self._head = current.next()
                else:
                    previous_node.append(current.next())
                return
            previous_node = current
            current = current.next()
        raise ValueError(f'No element with value {target} was found in the list')

    def search(self, target) -> Node.data:
        current = self._head
        while current is not None:
            if current.data() == target:
                return current.data()
            current = current.next()
        return None

        
    def traverse(self, functor):
        current = self._head
        result = []
        while current is not None:
            result.append(functor(current.data()))
            current = current.next()
        return result
    


