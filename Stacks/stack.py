from LinkedLists.singly_linked_list import SinglyLinkedList

class Stack:

    """
    In stacks, the way elements are inserted is important.
    The logic to implement is LIFO - Last In First Out.
        ->  It is important to have a low insrt time
        ->  i do not need to traverse or search, i just need to retrieve the last inserted element

    DynamicArray vs LinkedList - Worst Case:
    insert O(n) - insert_in_front O(1)
    get O(1) - head O(1)

    Also, I use SinglyLinkedList to save memory, as a backward pointer is not needed.
    """
    def __init__(self):
        self._data = SinglyLinkedList()

    def __repr__(self):
        if self.is_empty():
            return 'Stack([])'
        elements = []

        current = self._data._head
        while current:
            elements.append(current._data)
            current = current.next()
    
        return f'Stack({elements})'

    
    def is_empty(self):
        return self._data.is_empty()

    def Push(self, data):
        self._data.insert_in_front(data)
    
    def Pop(self):
        if self.is_empty():
            raise ValueError("Cannot pop from an empty stack")
        self._data.delete_from_front()

    def Peek(self):
        if self.is_empty():
            raise ValueError("Cannot peek from an empty stack")
        return self._data.get(0)