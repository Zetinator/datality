from typing import Any, List, Optional

from datality.bst import BST


class Node:
    """Node basic chainable storage unit"""

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class SplayTree(BST):
    """implementation of Tarjan's Splay Tree

    this is my favorite data structure :D
    the mighty dinamically optimal tree...

    https://en.wikipedia.org/wiki/Splay_tree
    """

    def __init__(self, values: List[Any] = []):
        self.root: Optional[Node] = None
        self.length: int = 0
        for value in values:
            self.insert(value)

    def insert(self, value):
        """insert a new node with the given `value` in the tree

        standard bst insertion + rotate till root
        """
        if not self.root:
            self.root = Node(value)
            # update length
            self.length += 1
            return

        def r(node: Node):
            """modified bst insertion
            making the inserted node root
            """
            if value == node.value:
                # already in the tree... do nothing
                self.length -= 1
                return
            if value < node.value:
                if node.left:
                    r(node.left)
                else:
                    node.left = Node(value)
                # went left? rotate back right :D
                self.rotate_right(node)
            else:
                if node.right:
                    r(node.right)
                else:
                    node.right = Node(value)
                # went right? rotate back left
                self.rotate_left(node)

        r(self.root)
        # update length
        self.length += 1

    def search(self, value: Any) -> Node:
        """standard binary search + rotations

        search also brings the searched node to root, part of the magic :D

        Args:
            value (Any): value to look fo in the tree

        Raises:
            KeyError: raised when the node is not found

        Returns:
            Node: node containing the given `value`
        """
        if not self.root:
            raise KeyError(f"{value} not found")

        def r(node):
            """bt + rotations"""
            if not node:
                raise KeyError(f"{value} not found")
            if value == node.value:
                return
            if value < node.value:
                r(node.left)
                # went left? rotate back right :D
                self.rotate_right(node)
            else:
                r(node.right)
                # went right? rotate back left
                self.rotate_left(node)

        r(self.root)
        # after the search the found node is the new root :O
        return self.root
