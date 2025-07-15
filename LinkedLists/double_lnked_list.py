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
    