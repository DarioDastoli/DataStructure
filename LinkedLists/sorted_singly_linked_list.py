from .singly_linked_list import SinglyLinkedList

class SortedSinglyLinkedList(SinglyLinkedList):
    def insert_in_sorted_list(self, data):
        current = self._head
        previous = None
        while current is not None:
            if current.data() >= data:
                if previous is None:
                    self._head = SinglyLinkedList.Node(data, current)    # Add the element at the beginning of the list
                else:
                    previous.append(SinglyLinkedList.Node(data, current))    # General case
                return
            previous = current
            current = current.next()
        if previous is None:
            self._head = SinglyLinkedList.Node(data)    # The list is empty
        else:
            previous.append(SinglyLinkedList.Node(data, None))    # Add the element at the end of the list