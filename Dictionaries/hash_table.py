from math import floor, sqrt
from decimal import Decimal
from LinkedLists.singly_linked_list import SinglyLinkedList
from typing import Any, Callable

class HashTable:
    __A__ = Decimal((sqrt(5) - 1) / 2) # The constant for the multiplication method, defined as a class property

    def __init__(self, buckets: int, extract_key:  Callable[..., Any]=hash) -> None:
        if buckets <= 0:
            raise ValueError(f'Invalid size for the hash table (must be positive): {buckets}')
        self._m = buckets
        self._data = [SinglyLinkedList() for _ in range(buckets)]
        self._extract_key = extract_key

    def _hash(self, key: int) -> int:
        return floor(self._m*((Decimal(key) * HashTable.__A__)%1))
    
    def insert(self, value):
        index = self._hash(self._extract_key(value))
        self._data[index].insert_in_front(value)

    def search(self, key) -> Any:
        index = self._hash(key)
        value_matches_key = lambda v: self._extract_key(v) == key
        return self._data[index].search(value_matches_key)

    def delete(self, value):
        index = self._hash(self._extract_key(value))
        self._data[index].delete(value)