class Queue:
    def __init__(self, max_size):
        if max_size <= 1:
            raise ValueError(f'Invalid size for a queue (must have at least 2 elements): {max_size}')
        self._data = [None] * max_size
        self._max_size = max_size
        self._front = 0
        self._rear = 0
        self._size = 0

    def __len__(self) -> int:
        return self._size
    
    def is_empty(self) -> bool:
        return len(self) == 0 
    
    def is_full(self) -> bool:
        return len(self) == self._max_size
    

    
    def enqueue(self, value):
        if self.is_full():
            raise ValueError('Queue is full')
        self._data[self._rear] = value
        self._rear = (self._rear + 1) % self._max_size
        self._size += 1
    

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Cannot dequeue from an empty queue")
        value = self._data[self._front]
        self._front = (self._front + 1) % self._max_size
        self._size -= 1
        return value
