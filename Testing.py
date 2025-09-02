from Arrays import core
from math import sqrt
from random import Random
from LinkedLists.singly_linked_list import SinglyLinkedList 
import copy

class Heap:
    """
    
    """
    def __init__(self, elements = None, element_priority = lambda x: x):
        self._priority = element_priority
        if elements is not None and len(elements) > 0:
            self._heapify(elements)
        else:
            self._elements = []

    def _has_lower_priority(self, element_1, element_2):
        return self._priority(element_1) < self._priority(element_2)
    def _has_higher_priority(self, element_1, element_2):
        return self._priority(element_1) > self._priority(element_2)
    def _left_child_index(self, index):
        return index * 2 + 1
    def _parent_index(self, index):
        return (index - 1) // 2
    
    def _bubble_up(self, index):
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
    
    def insert(self, element):
        self._elements.append(element)
        self._bubble_up(len(self._elements) - 1)
    
