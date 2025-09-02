from core import Array

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

"""
    Here both max_in_array and min_in_array have O(n) to find the max or the min in the array
"""

def max_in_array(array):
    if len(array) == 0:
        raise Exception('Max of an empty array')
    max_index = 0
    for index in range(0, self._size):
        if array[index] > array[max_index]:
            max_index = array[index]
    return max_index, array[max_index]

"""
EXERCISE 2.1
Write the code for a function returning the minimum value in an array and its index.
Hint: Can you adapt the function max_in_array?
"""
def min_in_array(array):
    if len(array) == 0:
        raise Exception('Min of an empty array')
    min_index = 0
    for index in range(0, len(array)):
        if array[index] < array[min_index]:
            min_index = array[index]
    return min_index, array[min_index]

"""    
EXERCISE 2.2
The advantage of using one function to find and return both, is that i only need to 
go throught the array once, we can get Min and Max in O(n)
"""

def min_and_max_in_array(array):
    if len(array) == 0:
        raise Exception('Min and Max of an empty array')
    min_index = 0
    max_index = 0
    for index in range(0, len(array)):
        if array[index] < array[min_index]:
            min_index = array[index]
        if array[index] > array[max_index]:
            max_index = array[index]
    return min_index, max_index

