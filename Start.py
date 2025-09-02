from Queues.queue import Queue


x = Queue(10)

x.enqueue(1)
x.enqueue(2)
x.enqueue(3)
x.enqueue(4)
x.enqueue(5)

a = x.peek()

print(f'a = {a}')

b = x.dequeue()
c = x.dequeue()

print(f'b = {b}')
print(f'c = {c}')
print(f'len = {len(x)}')

d = x.peek()

print(f'd = {d}')