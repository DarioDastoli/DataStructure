from LinkedLists.singly_linked_list import SinglyLinkedList

class Stack:
    def __init__(self):
        self._data = SinglyLinkedList()
    
    def push(self, value):
        self._data.insert_in_front(value)
    
    def pop(self):
        if self._data is None:
            raise ValueError("Cannot pop from an empty stack")
        return self._data.delete_from_front()
        
    def peek(self) -> SinglyLinkedList.Node:
        if self._data.is_empty():
            raise ValueError("Cannot peek at an empty stack")
        return self._data.get(0)
    
    def is_empty(self):
        return self._data.is_empty()