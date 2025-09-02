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


    """
    EXERCISE
    6.3 Can you think of a way to write the insert_in_sorted_list method by reusing
        the insert_in_front and delete methods and without making any other
        explicit changes to the nodes? What would be the running time of this method?
    """
    def insert_in_front_2(self, data):
        pass
        
