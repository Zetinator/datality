from typing import Any, Iterable, Optional

from datality.bst import BST


class Node:
    """node chainable storage unit"""

    def __init__(self, value: Any = None):
        self.value = value
        self.weight: int = 1
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


class AVL(BST):
    """implementation of the AVL

    https://en.wikipedia.org/wiki/AVL_tree
    """

    def __init__(self, values: Iterable[Any] = []):
        self.root: Optional[Node] = None
        self._length: int = 0
        for value in values:
            self.insert(value)

    def rotate_left(self, pivot: Node) -> None:
        """left rotation

        https://en.wikipedia.org/wiki/AVL_tree#Simple_rotation

        Args:
            pivot (Node): pivot of the rotation
        """
        aux_node = Node(pivot.value)
        aux_node.left, aux_node.right = pivot.left, pivot.right.left
        # replace
        pivot.value = pivot.right.value
        pivot.left, pivot.right = aux_node, pivot.right.right
        # update weights
        self.update_weight(pivot.left)
        self.update_weight(pivot)

    def rotate_right(self, pivot: Node) -> None:
        """right rotation

        https://en.wikipedia.org/wiki/AVL_tree#Simple_rotation

        Args:
            pivot (Node): pivot of the rotation
        """
        aux_node = Node(pivot.value)
        aux_node.left, aux_node.right = pivot.left.right, pivot.right
        # replace
        pivot.value = pivot.left.value
        pivot.left, pivot.right = pivot.left.left, aux_node
        # update weights
        self.update_weight(pivot.right)
        self.update_weight(pivot)

    def compute_weight(self, node: Node) -> int:
        """method to compute the weight of a node

        this function is simple just to deal with the None children

        Args:
            node (Node): node to update the weights

        Returns:
            int: the weight of the given node
        """

        return node.weight if node else 0

    def update_weight(self, node: Node) -> None:
        """method to update the weight of a node given the weights of its children

        the default weight of a new node is 1
        and the null node is 0 naturally...

        Args:
            node (Node): node to update the weights
        """
        node.weight = (
            max(self.compute_weight(node.left), self.compute_weight(node.right)) + 1
        )

    def insert(self, value: Any) -> None:
        """insert a new node into the bst, and rebalance

        Args:
            value (Any): must be comparable
        """
        # special case: empty bst
        if not self.root:
            self.root = Node(value)
            # update length
            self._length += 1
            return

        def r(current_node: Node, value: Any):
            """modified bst insertion"""
            if current_node.value == value:
                # if value already in the tree do nothing
                self._length -= 1
                return
            if value < current_node.value:
                if current_node.left:
                    r(current_node.left, value)
                else:
                    current_node.left = Node(value)
            else:
                if current_node.right:
                    r(current_node.right, value)
                else:
                    current_node.right = Node(value)
            # update the weights of each visited node
            self.update_weight(current_node)
            # compute balance_factor
            w_right = self.compute_weight(current_node.right)
            w_left = self.compute_weight(current_node.left)
            balance_factor = w_right - w_left
            # repair violations
            if balance_factor < -1:
                # rotate right
                if value > current_node.left.value:
                    # left - right
                    self.rotate_left(current_node.left)
                self.rotate_right(current_node)
                return
            if balance_factor > 1:
                # rotate left
                if value < current_node.right.value:
                    # right - left
                    self.rotate_right(current_node.right)
                self.rotate_left(current_node)
                return

        r(self.root, value)
        # update length
        self._length += 1

    def delete(self, value: Any) -> None:
        """search for value, and rotate until leaf, then delete

        Args:
            value (Any): value to delete

        Raises:
            KeyError: raised when the value is not in the tree
        """
        if value is None or not self.root:
            raise KeyError(f"{value} not found")

        def fetch(node: Node, parent: Node):
            """standard bst search but keeps track of the parents"""
            if not node:
                raise KeyError(f"{value} not found")
            if node.value == value:
                return (node, parent)
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
                    return
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
            # do not forget to update the weights
            self.update_weight(node)

        r(node, parent)
        # update length
        self._length -= 1
