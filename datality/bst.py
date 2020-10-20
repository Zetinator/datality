from typing import Any, List, Optional


class Node:
    """node chainable storage unit"""

    def __init__(self, value: Optional[Any] = None):
        self.value: Any = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


class BST:
    """custom implementation of a binary search tree

    https://en.wikipedia.org/wiki/Binary_search_tree
    """

    def __init__(self, values: List[Any] = []):
        self.root: Optional[Node] = None
        self.length: int = 0
        for value in values:
            self.insert(value)

    def insert(self, value: Any) -> None:
        """inserts a new node with the given `value`


        Args:
            value (Any): value to be inserted
        """
        # special case: empty tree
        if not self.root:
            self.root = Node(value)
            self.length += 1
            return

        def r(node: Node, value: Any):
            """standard bst insertion"""
            if node.value == value:
                # value already in the tree, do nothing
                self.length -= 1
                return
            if value < node.value:
                if node.left:
                    r(node.left, value)
                else:
                    node.left = Node(value)
            else:
                if node.right:
                    r(node.right, value)
                else:
                    node.right = Node(value)

        r(self.root, value)
        # update length
        self.length += 1

    def search(self, value: Any) -> Node:
        """searches the node with the given `value`

        https://en.wikipedia.org/wiki/Binary_search_tree#Searching

        Args:
            value (Any): value to look for

        Raises:
            KeyError: raised when the value is not found

        Returns:
            Node: Node containing the given `value`
        """
        # special case: empty tree
        if not self.root:
            raise KeyError(f"{value} not found")

        def r(node: Node):
            if not node:
                raise KeyError(f"{value} not found")
            if value == node.value:
                return node
            # keep looking
            if value < node.value:
                return r(node.left)
            else:
                return r(node.right)

        return r(self.root)

    def successor(self, value: Any) -> Node:
        """get the next in-order successor of a node with the given `value`

        Args:
            value (Any): value of the predecesor

        Raises:
            KeyError: raised when the value is not found

        Returns:
            Node: node containing the value of the successor
        """
        if not self.root:
            raise KeyError(f"successor of {value} not found")

        def r(node: Node, next_ancestor: Node):
            """find the node recursively, keep track of the anscestors"""
            if not node:
                raise KeyError(f"{value} not in the tree")
            if node.value == value:
                # found
                return (node, next_ancestor)
            # keep looking
            if value < node.value:
                return r(node.left, node)
            else:
                return r(node.right, next_ancestor)

        node, next_ancestor = r(self.root, None)
        # no right subtree, return the previous bigger ancestor
        if not node.right:
            if not next_ancestor:
                raise KeyError(f"{value} not in the tree")
            return next_ancestor
        # go all the way left in the right subtree to get the successor
        node = node.right
        while node.left:
            node = node.left
        if not node:
            raise KeyError(f"{value} not in the tree")
        return node

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

    def delete(self, value: Any) -> None:
        """deletes the node containinf the given `value`

        this is my favorite way of deletion is also optimal O(ln(n))

        Args:
            value (Any): value of the node to look for

        Raises:
            KeyError: raised when the value is not found
        """
        if value is None:
            raise KeyError(f"{value} not found")

        def fetch(node, parent):
            """recursively find the node to delete and his parent"""
            if not node:
                raise KeyError(f"{value} not found")
            if node.value == value:
                # found
                return (node, parent)
            # keep looking
            if value < node.value:
                return fetch(node.left, node)
            else:
                return fetch(node.right, node)

        node, parent = fetch(self.root, None)

        def r(node: Node, parent: Node):
            """when found, rotate the node until it becomes a leaf

            once a leaf deletion is trivial
            """
            if not node.left and not node.right:
                # special case: root
                if not parent:
                    self.root = None
                # actual deletion
                if node == parent.right:
                    parent.right = None
                    return
                else:
                    parent.left = None
                    return
            # rotate until leaf...
            child = node.left or node.right
            if child == node.left:
                self.rotate_right(node)
                # our node switches place with the right child
                r(node.right, node)
            else:
                self.rotate_left(node)
                # our node switches place with the left child
                r(node.left, node)

        r(node, parent)
        # update length
        self.length -= 1

    def __repr__(self):
        res = []

        def r(node: Node, level: int = 0):
            """modified in-order traversal"""
            if not node:
                return
            r(node.right, level + 1)
            res.append("\t" * level + f"-->({node.value})")
            r(node.left, level + 1)

        r(self.root)
        return "\n".join(res)

    def __len__(self):
        return self.length
