from typing import Any, Optional, Callable, List

class DoubleLinkedList:
    """
    A doubly linked list implementation.
    Classes:
        Node: Represents a node in the doubly linked list, containing data and pointers to the next and previous nodes.
    Methods:
        __init__():
            Initializes an empty doubly linked list.
        __str__(self) -> str: #O(n)
            Return the string representation of the linked list. 
        insert_in_front(data: Any) -> None: #O(1)
            Inserts a new node containing 'data' at the front (head) of the list.
        insert_at_back(data: Any) -> None: #O(1)
            Inserts a new node containing 'data' at the back (tail) of the list.
        is_empty() -> bool: #O(1)
            Returns True if the list is empty, False otherwise.
        delete_from_front() -> Any: #O(1)
            Removes and returns the data from the front node of the list.
            Raises ValueError if the list is empty.
        delete_from_back() -> Any: #O(1)
            Removes and returns the data from the back node of the list.
            Raises ValueError if the list is empty.
        delete(target: Any) -> None: #O(n)
            Removes the first node containing 'target' from the list.
            Raises ValueError if 'target' is not found.
        search(target: Any) -> Optional[Any]: #O(n)
            Searches for the first node containing 'target' and returns its data if found, otherwise returns None.
        traverse(functor: Callable[[Any], Any]) -> List[Any]: #O(n)
            Applies 'functor' to the data of each node in the list and returns a list of the results.
    """

    class Node:
    
        """
        A node in a doubly linked list.
        Attributes:
            _data (Any): The data stored in the node.
            _next (Optional[DoubleLinkedList.Node]): Reference to the next node in the list.
            _previous (Optional[DoubleLinkedList.Node]): Reference to the previous node in the list.
        Methods:
            __init__(data: Any) -> None:
                Initializes a new node with the given data.
            __str__(self) -> str:
                Returns the string representation of the node's data.
            data() -> Any:
                Returns the data stored in the node.
            next() -> Optional[DoubleLinkedList.Node]:
                Returns the next node in the list, or None if there is no next node.
            previous() -> Optional[DoubleLinkedList.Node]:
                Returns the previous node in the list, or None if there is no previous node.
            has_next() -> bool:
                Returns True if there is a next node, False otherwise.
            has_previous() -> bool:
                Returns True if there is a previous node, False otherwise.
            append(next_node: Optional[DoubleLinkedList.Node]) -> None:
                Sets the next node and updates the previous reference of the next node.
            prepend(prev_node: Optional[DoubleLinkedList.Node]) -> None:
                Sets the previous node and updates the next reference of the previous node.
        """

        def __init__(self, data: Any) -> None:
            self._data: Any = data
            self._next: Optional['DoubleLinkedList.Node'] = None
            self._previous: Optional['DoubleLinkedList.Node'] = None

        def __str__(self) -> str:
            return str(self.data())

        def data(self) -> Any:
            return self._data
        
        def next(self) -> Optional['DoubleLinkedList.Node']:
            return self._next
        
        def previous(self) -> Optional['DoubleLinkedList.Node']:
            return self._previous
        
        def has_next(self) -> bool:
            return self.next() is not None
        
        def has_previous(self) -> bool:
            return self._previous is not None
        
        def append(self, next_node: Optional['DoubleLinkedList.Node']) -> None:
            self._next = next_node
            if next_node is not None:
                next_node._previous = self

        def prepend(self, prev_node: Optional['DoubleLinkedList.Node']) -> None:
            self._previous = prev_node
            if prev_node is not None:
                prev_node._next = self

    def __init__(self) -> None:
        self._head: Optional['DoubleLinkedList.Node'] = None
        self._tail: Optional['DoubleLinkedList.Node'] = None

    def __str__(self) -> str:
        return f'DoublyLinkedList({"<->".join(self.traverse(repr))})'

    def insert_in_front(self, data: Any) -> None:
        if self._head is None:
            self._tail = self._head = DoubleLinkedList.Node(data)
        else:
            old_head = self._head
            self._head = DoubleLinkedList.Node(data)
            self._head.append(old_head)

    def insert_at_back(self, data: Any) -> None:
        if self._tail is None:
            self._tail =  self._head = DoubleLinkedList.Node(data)
        else:
            old_tail = self._tail
            self._tail = DoubleLinkedList.Node(data)
            self._tail.prepend(old_tail)

    def is_empty(self) -> bool:
        return self._head is None
    
    def delete_from_front(self) -> Any:
        if self._head is None:
            raise ValueError('Delete on an empty list')
        data = self._head.data()
        self._head = self._head.next()
        return data
    
    def delete_from_back(self) -> Any:
        if self._tail is None:
            raise ValueError('Delete on an empty list')
        data = self._tail.data()
        if self._tail._previous is not None:
            self._tail = self._tail._previous
            self._tail._next = None
        else:
            self._head = self._tail = None
        return data
    
    def delete(self, target: Any) -> None:
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

    def search(self, target: Any) -> Optional[Any]:
        current = self._head
        while current is not None:
            if current.data() == target:
                return current.data()
            current = current.next()
        return None

        
    def traverse(self, functor: Callable[[Any], Any]) -> List[Any]:
        current = self._head
        result = []
        while current is not None:
            result.append(functor(current.data()))
            current = current.next()
        return result

    def insert_middle(self, target, new_node: 'DoubleLinkedList.Node'):
        current = self._head
        while current is not None:
            if current.data() == target:
                new_node.append(current.next())
                current.append(new_node)
                if current == self._tail:
                    self._tail = new_node
                return
            current = current.next()
        raise ValueError(f'No element with value {target} was found in the list')