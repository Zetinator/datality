from random import uniform
from typing import Any, Iterable, Optional

from datality.bst import BST


class Node:
    """Node basic chainable storage unit"""

    def __init__(self, value=None):
        self.value = value
        self.priority = uniform(0, 1)
        self.left = None
        self.right = None


class Treap(BST):
    """implementation of the Treap (bst + heap)

    https://en.wikipedia.org/wiki/Treap
    """

    def __init__(self, values: Iterable[Any] = []):
        self.root: Optional[Node] = None
        self._length: int = 0
        for value in values:
            self.insert(value)

    def rotate_right(self, node: Node) -> None:
        """right rotation

        https://en.wikipedia.org/wiki/AVL_tree#Simple_rotation
        """
        _ = Node(node.value)
        # dont forget the priority
        _.priority = node.priority
        _.left, _.right = node.left.right, node.right
        # rotate...
        node.value, node.priority = node.left.value, node.left.priority
        node.left, node.right = node.left.left, _

    def rotate_left(self, node: Node) -> None:
        """left rotation

        https://en.wikipedia.org/wiki/AVL_tree#Simple_rotation
        """
        _ = Node(node.value)
        # dont forget the priority
        _.priority = node.priority
        _.left, _.right = node.left, node.right.left
        # rotate...
        node.value, node.priority = node.right.value, node.right.priority
        node.left, node.right = _, node.right.right

    def insert(self, value: Any) -> None:
        """insert a new node with the given `value` in the tree

        standard bst insertion + rotations to keep the mighty heap invariance

        Args:
            value (Any): must be comparable
        """
        if not self.root:
            self.root = Node(value)
            # update length
            self._length += 1
            return

        def r(node):
            """modified bst insertion"""
            if value == node.value:
                # already in the tree do nothing...
                self._length -= 1
                return
            if value < node.value:
                if node.left:
                    r(node.left)
                else:
                    node.left = Node(value)
            else:
                if node.right:
                    r(node.right)
                else:
                    node.right = Node(value)
            # repair max_heap invariants...
            if value > node.value:
                if node.right.priority > node.priority:
                    self.rotate_left(node)
            else:
                if node.left.priority > node.priority:
                    self.rotate_right(node)

        r(self.root)
        # update length
        self._length += 1

    def delete(self, value: Any) -> None:
        """search and delete the node with the given `value` in the tree

        rotate the node to be deleted with the max child
        until it becomes a leaf, then deletion is trivial...
        """
        # standard binary search for the node, and the parent
        if not self.root:
            raise KeyError(f"{value} not found")

        def get(node, parent):
            if not node:
                raise KeyError(f"{value} not found")
            if value == node.value:
                return (node, parent)
            if value < node.value:
                return get(node.left, node)
            else:
                return get(node.right, node)

        node, parent = get(self.root, None)

        def r(node, parent):
            """standard bst search but keeps track of the parents"""
            if not node.left and not node.right:
                # special case: root
                if not parent:
                    self.root = None
                    return
                # actual deletion
                if parent.right == node:
                    parent.right = None
                    return
                else:
                    parent.left = None
                    return
            # rotate with max_child, until no childs remain...

            def priority(node):
                return node.priority if node else -float("inf")

            max_child = max(node.left, node.right, key=lambda node: priority(node))
            if max_child == node.right:
                self.rotate_left(node)
                return r(node.left, node)
            else:
                self.rotate_right(node)
                return r(node.right, node)

        r(node, parent)
        # update length
        self._length -= 1
