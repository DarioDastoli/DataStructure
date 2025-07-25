from core import Array
from typing import Union

class SortedArray():
    def __init__(self, max_size, typecode = 'l'):
        self._array = Array(max_size, typecode)
        self._max_size = max_size
        self._size = 0

    def __len__(self) -> int:
        return self._size
    
    def __getitem__(self, index) -> Union[int, float]:

        if index < 0 or index >= self._size:
            raise IndexError(f'Index out of bound: {index}')
        return self._array[index]
    
    def __repr__(self) -> str:

        return f'UnsortedArray({repr(self._array._array[:self._size])})'
    
    def __iter__(self):
        '''
        Iterate over the values in the sorted array.

        Parameters:
            None

        Functionality:
            Iterates over the values in the sorted array. The iteration starts at index 0 and
            goes on until it reaches the end of the array (not the full maximum capacity of the array,
            just the last stored elements).
        '''

        for i in range(self._size):
            yield self._array[i]

    
    def insert(self, value):
        if self._size >= self._max_size:
            raise ValueError(f'The array is already full, maximum size : {self._max_size}')
        for i in range(self._size, 0, -1): #parti da self._size(), fermati a  0, incrementa di -1 
            if self._array[i-1] <= value:
                self._array[i] = value
                self._size += 1
                return
            else:
               self._array[i] = self._array[i-1]
        self._array[0] = value
        self._size += 1
    
    def delete(self, target):
        index = self.binary_search(target)
        if index is None:
            raise ValueError(f'unable to delete element {target}: the entry is not in the array')
        for i in range(index, self._size - 1):
            self._array[i] = self._array[i + 1]
        self._size -=1

    def delete_by_index(self, index):
        for i in range(index, self._size - 1):
            self._array[i] = self._array[i + 1]
        self._size -=1

    def linear_search(self, target) -> int:
        for i in range(self._size):
            if self._array[i] > target:
                return None
            if self._array[i] == target:
                return i
        return None
    
    def binary_search(self, target) -> int:
        left = 0
        right = self._size - 1
        while left <= right:
            mid_index = (left + right) // 2
            mid_val = self._array[mid_index]
            if target == mid_val:
                return mid_index
            elif target > mid_val:
                left = mid_index + 1
            elif target < mid_val:
                right = mid_index - 1
        return None
    
    def traverse(self, callback):
        for index in range(0, self._size):
            callback(self._array[index])

