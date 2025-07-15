from Stacks.stack import *
from Queues import *
from LinkedLists.double_lnked_list import DoubleLinkedList 
s = DoubleLinkedList()

for i in range(7):
    s.insert_in_front(i)

x = s.search(2)
s.traverse(print)
print('----------------------------')

print(x)

print('----------------------------')

s.delete_from_front()
s.traverse(print)
print('----------------------------')

y = s.delete_from_back()

print(y)
print('----------------------------')

s.traverse(print)
print('----------------------------')


s.delete(2)
s.traverse(print)
print('----------------------------')



