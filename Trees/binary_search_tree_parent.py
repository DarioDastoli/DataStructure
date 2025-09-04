"""
Binary search tree (BST) implementation 

EXERCISES
11.1 Implement a BST class where nodes contain a link to their parent, and then add the
    predecessor and successor methods.
11.2 Can you find an example among the BSTs shown in the previous sections where the
    predecessor method described above would fail? Hint: Refer to the next
    exercise.
11.3 When a BST contains duplicates, then getting the predecessor of a node is a bit
    more complicated, while the successor method can work as it is. Can you explain
    why?
11.4 How can we fix the predecessor method to deal with duplicates?
"""

class BinarySearchTreeParent:
    """
    A class representing a Binary Search Tree (BST) data structure.
    The BinarySearchTree supports insertion, deletion, and search operations,
    maintaining the BST property where for any given node, all values in the left
    subtree are less than or equal to the node's value, and all values in the right
    subtree are greater.
    Inner Classes:
        Node: Represents a node in the binary search tree, containing a value and
              references to left and right child nodes.
    Methods:
        __init__():
            Initializes an empty binary search tree.
        __repr__():
            Returns a string representation of the binary search tree.
        _search(value):
            Searches for a node with the specified value.
            Returns a tuple (node, parent) if found, otherwise (None, None).
        insert(value):
            Inserts a value into the binary search tree, maintaining BST properties.
        delete(value):
            Deletes a node with the specified value from the tree.
            Raises ValueError if the tree is empty or the value is not found.
        print_tree(node=None, level=0, prefix="Root: "):
            Prints the tree structure in a visual format, starting from the given node.
            If no node is specified, prints from the root.
    """
    class Node:
        def __init__(self, value, left=None, right=None, parent=None) -> None:
            self._value = value
            self._left = left
            self._right = right
            self._parent = parent

        def set_left(self, node) -> None:
            self._left = node
        
        def get_left(self) -> 'BinarySearchTreeParent.Node':
            return self._left
        
        def value(self):
            return self._value
        
        def set_right(self, node) -> None:
            self._right = node
        
        def get_right(self)-> 'BinarySearchTreeParent.Node':
            return self._right
        
        def set_parent(self, node: 'BinarySearchTreeParent.Node') -> None:
            self._parent = node._parent
        
        def get_parent(self) -> 'BinarySearchTreeParent.Node':
            return self._parent

    def __init__(self) -> None:
        self._root: BinarySearchTreeParent.Node = None

    def __repr__(self) -> str:
        return f'BinarySearchTree({str(self)})'        

    def _search(self, value) -> 'BinarySearchTreeParent.Node':

        node = self._root
        while node is not None:
            node_value = node.value()
            if node_value == value:
                return node #  target found!
            elif value < node_value:           
                node = node.get_left()
            else:
                node = node.get_right()
        return None # target not found
    
    def insert(self, value):
        node = self._root
        parent = None
        if node is None:
            self._root = BinarySearchTreeParent.Node(value)
        else:
            parent = self._root
            while True:
                if value <= node.value():
                    if node.get_left() is None:
                        node.set_left(BinarySearchTreeParent.Node(value, parent=parent))
                        break
                    else:
                        node = node.get_left()
                elif value > node.value():
                    if node.get_right() is None:
                        node.set_right(BinarySearchTreeParent.Node(value, parent=parent))
                        break
                    else:
                        node = node.get_right()
                parent = node


    def delete(self, value):
        if self._root is None:
            raise ValueError('Delete on an empty tree')
        node = self._search(value)
        if node is None:
            raise ValueError('Value not found')

        if node.left() is None or node.right() is None:
            maybe_child = node.right() if node.left() is None else node.left()
            # The node has at most only one child
            if node._parent is None:
                # The node is the root
                self._root = maybe_child
            elif value <= node._parent.value():
                node._parent.set_left(maybe_child)
            else:
                node._parent.set_right(maybe_child)
        else: # The node N has two children.
            # Find and remove the node M with the largest value in the left subtree of N.
            max_node, max_node_parent = node.left().find_max_in_subtree()
            if max_node_parent is None: # M is the left child of N.
                new_node = BinarySearchTreeParent.Node(max_node.value(), None, node.right())
            else:
                new_node = BinarySearchTreeParent.Node(max_node.value(), node.left(), node.right())
                max_node_parent.set_right(max_node.left())
            # Then  replace the node to be deleted with a new node with M.value(),
            # and the same subtrees as N.
            if node._parent is None:
                # The node is the root
                self._root = new_node
            elif value <= node._parent.value():
                node._parent.set_left(new_node)
            else:
                node._parent.set_right(new_node)

    def predecessor(self, value) -> any:
        if self._root is None:
            raise ValueError('No predecessor in an empty tree')
        node = self._search(value)
        parent = node.get_parent()
        if node.get_left() is not None:
            left_subtree_root =  node.get_left()
            left_subtree_node = left_subtree_root
            if left_subtree_root is not None:
                while left_subtree_node.get_right() is not None :
                    left_subtree_node = left_subtree_node.get_right()
                return left_subtree_node.value()                
        if node.get_left() is None:
            if parent.get_right() is not None and parent.get_right().value() == value:
                return parent.value()
            elif parent.get_left().value() == value:
                while parent.get_parent() is not None:
                    climber = parent.get_parent()
                    if climber is self._root:
                        return None
                    if climber.get_right() is not None:
                        return climber.get_right().value()
                    
    def successor(self, value) -> any:
        pass
        if self._root is None:
            raise ValueError('No successor in an empty tree')
        node = self._search(value)
        if node.get_right() is not None:
            right_subtree_root =  node.get_right()
            left_subtree_node = right_subtree_root
            while left_subtree_node.get_left() is not None:
                left_subtree_node = left_subtree_node.get_left()
            return left_subtree_node.value()
        elif node.get_parent() is not None:
            parent = node.get_parent()
            while parent.value() <= node.value():
                parent = parent.get_parent()
            return parent.value()

            


        



                

        
                
    def print_tree(self, node=None, level=0, prefix="Root: "):
        """Print the tree structure in a visual format. Thanks GP"""
        if node is None:
            node = self._root
        
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.value()))
            
            if node.get_left() is not None or node.get_right() is not None:
                if node.get_left() is not None:
                    self.print_tree(node.get_left(), level + 1, "L--- ")
                else:
                    print(" " * ((level + 1) * 4) + "L--- None")
                
                if node.get_right() is not None:
                    self.print_tree(node.get_right(), level + 1, "R--- ")
                else:
                    print(" " * ((level + 1) * 4) + "R--- None")
        else:
            print("Tree is empty")