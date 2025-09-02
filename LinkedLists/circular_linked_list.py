"""EXERCISE
6.6 Implement a circular linked list, with step-by-step traversal. You can implement
either a singly or doubly linked version. 
Can we reuse anything from the classes we have defined earlier in the chapter? - i am resuing Doub
Is composition an option? 
Is inheritance an option, and what are pros and cons here?"""
from LinkedLists.double_lnked_list import DoubleLinkedList
from typing import Any, Optional

class CircularLinkedList:

    def __init__(self):
        self._data = DoubleLinkedList()
        
    def insert(self, value: Any) -> None:
        self._data.insert_at_back(value)
        if self._data._head is not None:
            self._data._tail.append(self._data._head)

    def traverse(self, functor) -> list | None:
        if self._data._head is None:
            return None
        current = self._data._head
        result = []
        while True:
            result.append(functor(current.data()))
            current = current.next()
            if current == self._data._head:
                break
        return result

    def insert_after_node(self, target_node:DoubleLinkedList.Node, new_node: DoubleLinkedList.Node) -> None:
        if self._data._head is None:
            return None
        current = self._data._head
        while current is not None:
            if current == target_node:
                new_node.append(current.next())
                new_node.prepend(current)
                if current == self._data._tail:
                    self._data._tail = new_node
                return
            current = current.next()
        raise ValueError(f'No element with value {target_node.data()} was found in the list')
    
