"""Binary search tree (BST) implementation """

class BinarySearchTree:
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
        def __init__(self, value, left=None, right=None) -> None:
            self._value = value
            self._left = left
            self._right = right

        def set_left(self, node) -> None:
            self._left = node
        
        def get_left(self):
            return self._left
        
        def value(self):
            return self._value
        
        def set_right(self, node) -> None:
            self._right = node
        
        def get_right(self):
            return self._right

    def __init__(self) -> None:
        self._root: BinarySearchTree.Node = None

    def __repr__(self) -> str:
        return f'BinarySearchTree({str(self)})'        

    def _search(self, value):
        parent = None # we start from the root and the parent is None
        node = self._root
        while node is not None:
            node_value = node.value()
            if node_value == value:
                return node, parent #  target found!
            elif value < node_value:
                parent = node            
                node = node.get_left()
            else:
                parent = node
                node = node.get_right()
        return None, None # target not found
    
    def insert(self, value):
        node = self._root
        if node is None:
            self._root = BinarySearchTree.Node(value)
        else:
            while True:
                if value <= node.value():
                    if node.get_left() is None:
                        node.set_left(BinarySearchTree.Node(value))
                        break
                    else:
                        node = node.get_left()
                elif value > node.value():
                    if node.get_right() is None:
                        node.set_right(BinarySearchTree.Node(value))
                        break
                    else:
                        node = node.get_right()


    def delete(self, value):
        if self._root is None:
            raise ValueError('Delete on an empty tree')
        node, parent = self._search(value)
        if node is None:
            raise ValueError('Value not found')

        if node.left() is None or node.right() is None:
            maybe_child = node.right() if node.left() is None else node.left()
            # The node has at most only one child
            if parent is None:
                # The node is the root
                self._root = maybe_child
            elif value <= parent.value():
                parent.set_left(maybe_child)
            else:
                parent.set_right(maybe_child)
        else: # The node N has two children.
            # Find and remove the node M with the largest value in the left subtree of N.
            max_node, max_node_parent = node.left().find_max_in_subtree()
            if max_node_parent is None: # M is the left child of N.
                new_node = BinarySearchTree.Node(max_node.value(), None, node.right())
            else:
                new_node = BinarySearchTree.Node(max_node.value(), node.left(), node.right())
                max_node_parent.set_right(max_node.left())
            # Then  replace the node to be deleted with a new node with M.value(),
            # and the same subtrees as N.
            if parent is None:
                # The node is the root
                self._root = new_node
            elif value <= parent.value():
                parent.set_left(new_node)
            else:
                parent.set_right(new_node)

        
                
    def print_tree(self, node=None, level=0, prefix="Root: "):
        """Print the tree structure in a visual format"""
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