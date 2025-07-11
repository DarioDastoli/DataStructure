from core import Array
from typing import Union

class DinamicArray():
    def __init__(self, initial_capacity = 1, typecode = 'l'):
        self._array = Array(initial_capacity, typecode)
        self._capacity = initial_capacity
        self._size = 0
        self._typecode = typecode

    def _double_size(self):
        old_array = self._array #mi creo una copia del array
        self._array = Array(self._capacity * 2, typecode = self._typecode) #mi istanzio un nuovo self.array con la capacità raddoppiata
        self._capacity *= 2
        for i in range(self._size):
            self._array[i] = old_array[i] #copio il vecchio nel nuovo 

    def insert(self, value):
        if self._size >= self._capacity:
            self._double_size()
        self._array[self._size] = value
        self._size += 1

    def find(self, target):
        for index in range(self._size):
            if self._array[index] == target:
                return index
        return None

    def delete(self, value):
        index = self.find(value)
        if index == None:
            raise ValueError(f'Unable to delete element {value}: the entry is not in the array.')
        for i in range(index, self._size - 1):
            self._array[i] = self._array[i + 1]
        self._size -=1

    def traverse(self, callback):
        for index in range(0, self._size):
            callback(self._array[index])