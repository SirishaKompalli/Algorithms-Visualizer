
# Part of Cosmos by OpenGenus Foundation
class Node:
    """Base class to contain the tree metadata per instance of the class"""
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.data = val
def treeSort(root, node):
    """This recursive function will insert the objects into the tree"""
    if root is None:  # If we don't have a root node
        root = node  # Set the root node equal to the first node argument that was provided
    else:  # We already have a root
        if root.data > node.data:  # If our current root is bigger than the node we are about to insert
            if root.l_child is None:  # If we don't have any node to the left of root
                root.l_child = node  # Insert the node as the left node under root
            else:  # There's already a node to the left of root
                treeSort(
                    root.l_child, node
                )  # Call the insert function recursively with the left node value as the
                # temp root for comparison
        else:  # Node to be inserted is bigger than root (going right side)
            if root.r_child is None:  # if there's no right child
                root.r_child = node  # insert the node as the right child of root (under)
            else:  #
                treeSort(
                    root.r_child, node
                )  # Call the insert function recursively with the right node value as the
                # temp root for comparison
def post_sort_print(root):
    if not root:
        return None
    post_sort_print(root.l_child)
    print(root.data)
    post_sort_print(root.r_child)
def pre_sort_print(root):
    if not root:
        return None
    print(root.data)
    pre_sort_print(root.l_child)
    pre_sort_print(root.r_child)
