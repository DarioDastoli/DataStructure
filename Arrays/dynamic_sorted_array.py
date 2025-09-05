from Arrays.sorted_array import SortedArray
class DynamicSortedArray:
    def __init__(self, capacity = 1, typecode = 'l'):
        self._array = SortedArray(capacity)
        self._capacity = capacity
        self._size = 0
        self._typecode = typecode

    def __len__(self) -> int:
        return self._size
    
    def __getitem__(self, index):

        if index < 0 or index >= self._size:
            raise IndexError(f'Index out of bound: {index}')
        return self._array[index]
    
    def __repr__(self):
        elements = [self._array[i] for i in range(self._size)]
        return f'DynamicSortedArray {elements}'
    
    def _double_size(self):
        new_array = SortedArray(self._capacity * 2, self._typecode) #1
        for i in range(0, self._size): #n
            new_array.insert(self._array[i]) #1
        self._array = new_array #1
        self._capacity *= 2  #1
        print(f'capacity doubled= {self._capacity}')

    def _shrink_size(self):
        new_array = SortedArray(self._capacity // 2, self._typecode) #1
        for i in range(0, self._size): #n
            new_array.insert(self._array[i]) #1
        self._array = new_array #1
        self._capacity /= 2  #1
        print(f'capacity shrink= {self._capacity}')
    
    def insert(self, value):
        if self._size >= self._capacity:
            self._double_size()
        self._array.insert(value)
        self._size += 1

    def delete(self, value):
        index = self._array.binary_search(value)
        self._array.delete_by_index(index)
        self._size -= 1

        if self._size == self._capacity // 4:
            self._shrink_size()