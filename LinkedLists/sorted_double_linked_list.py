from typing import Any, Optional, Callable, List
from double_lnked_list import DoubleLinkedList

class SortedDLL(DoubleLinkedList):
    def insert_in_sorted_list(self, data):
        current = self._head
        previous = None

        while current is not None:
            if current.data() >= data:
                if previous is None:
                    self._head = DoubleLinkedList.Node(data)
                else:
                    self._previous - DoubleLinkedList.Node(data)
        previous = current
        current = current.next()
        if previous is None:
            self._head = DoubleLinkedList.Node(data)
        else:
            previous.append(DoubleLinkedList.Node(data))