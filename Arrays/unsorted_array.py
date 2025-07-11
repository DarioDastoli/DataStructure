from core import Array
from typing import Union

class UnsortedArray:
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
    
    def insert(self, new_entry):
        if self._size >= len(self._array):
            raise ValueError('The array is already full')
        else:
            self._array[self._size] = new_entry
            self._size += 1

    def delete(self, index):
        if self.size == 0:
            raise ValueError('Delete from an empty array')
        elif index < 0 or index >= self._size:
            raise ValueError(f'Index {index} out of range')
        else:
            self._array[index] = self._array[self._size - 1]
            self._size -= 1

    def find(self, target):
        for index in range(0, self._size):
            if self._array[index] == target:
                return index
        return None

    def traverse(self, callback):
        for index in range(0, self._size):
            callback(self._array[index])

