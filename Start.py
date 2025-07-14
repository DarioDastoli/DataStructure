from Stacks.stack import *
from Queues.queue_with_stacks import Queue
s = Queue()

for i in range(4):
    s.push(i)

s.traverse(print)
print('-------------------')
s.pop()
s.traverse(print)
print('-------------------')

s.push(20)
s.traverse(print)

s.pop()
s.traverse(print)
print('-------------------')
s.pop()
s.traverse(print)
print('-------------------')
s.pop()
s.traverse(print)
print('-------------------')
