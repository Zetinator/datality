from typing import Any, List, Optional

from datality.bst import BST


class Node:
    """node basic chainable storage unit"""

    def __init__(self, value: Any = None, color: str = "r"):
        self.value = value
        self.color = color
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


class RBTree(BST):
    """implementation of the red and black trees from Rudolf Bayer

    https://en.wikipedia.org/wiki/Red%E2%80%93black_tree
    """

    def __init__(self, values: List[Any] = []):
        self.root: Optional[Node] = None
        self.length: int = 0
        for value in values:
            self.insert(value)

    def insert(self, value: Any) -> None:
        """insert a new node with the given `value` into the tree

        Args:
            value (Any): value to be inserted
        """
        # special case: empty tree
        if not self.root:
            self.root = Node(value, color="b")
            # update length
            self.length += 1
            return

        def r(node: Node, parent: Node):
            """modified bst insertion"""
            if value == node.value:
                # already in the tree? do nothing
                self.length -= 1
                return
            if value < node.value:
                if node.left:
                    r(node.left, node)
                else:
                    node.left = Node(value)
            else:
                if node.right:
                    r(node.right, node)
                else:
                    node.right = Node(value)
            # repair violations to rb_tree's invariants... 4 special cases
            # special case 1: just make sure root remains black...
            if not parent:
                node.color = "b"
                return
            # special case 2: no further violations...
            elif node.color == "b":
                return
            # special case 3: uncle is red -> recolor
            elif self.brother(node, parent).color == "r":
                parent.color = "r"
                node.color = self.brother(node, parent).color = "b"
                return
            # special case 4: uncle is black -> rotate
            else:
                if parent.left == node:
                    # rotate right
                    if value > node.value:
                        # left -> right
                        self.rotate_left(node)
                    self.rotate_right(parent)

                else:
                    # rotate left
                    if value < node.value:
                        # right -> left
                        self.rotate_right(node)
                    self.rotate_left(parent)
                # switch colors parent <-> brother
                bro = self.brother(node, parent)
                parent.color, bro.color = bro.color, parent.color

        r(self.root, None)
        # update length
        self.length += 1

    def brother(self, node: Node, parent: Node) -> Node:
        """aux funtion to fetch my brother

        Args:
            node (Node): current node
            parent (Node): parent of the current node

        Returns:
            Node: the brother
        """
        # special case: root
        if not parent:
            return Node(color="b")
        bro = parent.left if parent.right == node else parent.right
        return bro or Node(color="b")

    def rotate_right(self, node: Node) -> None:
        """right rotation, on a given `node`

        https://en.wikipedia.org/wiki/AVL_tree#Simple_rotation

        Args:
            node (Node): pivot of the rotation
        """
        tmp = Node(node.value)
        tmp.left, tmp.right = node.left.right, node.right
        # rotate...
        node.value = node.left.value
        node.left, node.right = node.left.left, tmp

    def rotate_left(self, node):
        """left rotation, on a given `node`

        https://en.wikipedia.org/wiki/AVL_tree#Simple_rotation

        Args:
            node (Node): pivot of the rotation
        """
        tmp = Node(node.value)
        tmp.left, tmp.right = node.left, node.right.left
        # rotate...
        node.value = node.right.value
        node.left, node.right = tmp, node.right.right
