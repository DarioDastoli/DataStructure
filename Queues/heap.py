from typing import Any, Optional

class Heap:
    """
    A generic heap (priority queue) implementation.
    By default, it behaves as a max-heap, but can be configured for min-heap or other orderings.
    Args:
        elements (Optional[list]): Initial elements to build the heap from.
        element_priority (Callable): Function to determine the priority of each element.
    Methods:
        is_empty() -> bool:
            Returns True if the heap contains elements, False otherwise.
        insert(element) -> None:
            Inserts a new element into the heap, maintaining the heap property.
        top() -> Any:
            Returns the element with the highest priority.
            Raises ValueError if called on an empty heap.
    Internal Methods:
        _has_lower_priority(element_1, element_2) -> bool:
            Returns True if element_1 has lower priority than element_2.
        _has_higher_priority(element_1, element_2) -> bool:
            Returns True if element_1 has higher priority than element_2.
        _left_child_index(index: int) -> int:
            Returns the index of the left child for a given node index.
        _parent_index(index: int) -> int:
            Returns the index of the parent for a given node index.
        _bubble_up(index: int) -> None:
            Moves an element up the heap to restore the heap property.
        _highest_priority_child_index(index) -> Optional[int]:
            Returns the index of the child with the highest priority.
        _push_down(index) -> None:
            Moves an element down the heap to restore the heap property.
        _heapify(elements) -> None:
            Builds the heap from a list of elements.
        _first_leaf_index() -> int:
            Returns the index of the first leaf node in the heap.
    """

    def __init__(self, elements=None, element_priority=lambda x: x) -> None:
        self._priority = element_priority
        if elements is not None and len(elements) > 0:
            self._heapify(elements)
        else:
            self._elements = []

    def _has_lower_priority(self, element_1, element_2) -> bool:
        return self._priority(element_1) < self._priority(element_2) 
    
    def _has_higher_priority(self, element_1, element_2) -> bool:
        return self._priority(element_1) > self._priority(element_2) 
    
    def _left_child_index(self, index: int):
        return index * 2 + 1
    
    def _parent_index(self, index: int):
        return (index - 1) // 2
    
    def _bubble_up(self, index: int) -> None:
        element = self._elements[index]
        while index > 0:
            parent_index = self._parent_index(index)
            parent = self._elements[parent_index]
            if self._has_higher_priority(element, parent):
                self._elements[index] = parent
                index = parent_index
            else:
                break
        self._elements[index] = element
    
    def _highest_priority_child_index(self, index) -> Optional[Any]:
        first_index = self._left_child_index(index)
        if first_index >= len(self):
            return None
        if first_index + 1 >= len(self):
            return first_index  
        if self._has_higher_priority(self._elements[first_index], self._elements[first_index + 1]):
            return first_index
        else:
            return first_index + 1
        
    def _push_down(self, index) -> None:
        element = self._elements[index]
        current_index = index
        while True:
            child_index = self._highest_priority_child_index(current_index)
            if child_index is None:
                break
            if self._has_lower_priority(element, self._elements[child_index]):
                self._elements[current_index] = self._elements[child_index]
                current_index = child_index
            else:
                break
        self._elements[current_index] = element
    
    def _heapify(self, elements):
        self._elements = elements[:]
        last_inner_node_index = self._first_leaf_index() - 1
        for index in range(last_inner_node_index, -1, -1):
            self._push_down(index)

    def _first_leaf_index(self):
        return len(self) // 2 
    
    def is_empty(self) -> bool:
        return self._elements is not None and len(self._elements) > 0
    
    def insert(self, element) -> None:
        self._elements.append(element)
        self._bubble_up(len(self._elements) - 1)

    

    def top(self) -> Any:
        if self.is_empty():
            raise ValueError('Method top called on an empty heap.')
        if len(self) == 1:
            element = self._elements[0]
            self._elements[0] = self._elements.pop()
            self._push_down(0)
        return element
    

    
    