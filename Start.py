# from Queues.queue import Queue


# x = Queue(10)

# x.enqueue(1)
# x.enqueue(2)
# x.enqueue(3)
# x.enqueue(4)
# x.enqueue(5)

# a = x.peek()

# print(f'a = {a}')

# b = x.dequeue()
# c = x.dequeue()

# print(f'b = {b}')
# print(f'c = {c}')
# print(f'len = {len(x)}')

# d = x.peek()

# print(f'd = {d}')

from Trees.binary_search_tree_parent import BinarySearchTreeParent

bst = BinarySearchTreeParent()

bst.insert(6)
bst.insert(4)
bst.insert(2)
bst.insert(5)
bst.insert(1)
bst.insert(3)
bst.insert(7)
bst.insert(9)
bst.insert(8)



bst.print_tree()

a = bst.predecessor(8)
b = bst.successor(8)

print(f'predecessor - {a}')
print(f'successor - {b}')