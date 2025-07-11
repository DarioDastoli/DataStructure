from unsorted_array import *
from sorted_array import *


a = SortedArray(10)
for i in range(9):
    a.insert(i)

a.traverse(print)

a.delete_by_index(4)
a.traverse(print)
a.delete(8)
a.traverse(print)