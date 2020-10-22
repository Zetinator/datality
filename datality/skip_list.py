from random import uniform
from typing import Any, Iterable


class Node:
    """Node basic chainable storage unit"""

    def __init__(self, value: Any = None):
        self.value = value
        self.next = None
        self.down = None


class SkipList:
    """implementation of the skip list

    this is my second favorite data structure :D

    https://en.wikipedia.org/wiki/Skip_list
    https://www.youtube.com/watch?v=2g9OSRKJuzM
    """

    def __init__(self, values: Iterable[Any] = [], probability: float = 0.5):
        """constructor

        Args:
            values (Iterable[Any], optional): from list of values. Defaults to [].
            probability (float, optional): promotions probability. Defaults to .5.
        """
        self.root = Node(-float("inf"))
        self.probability: float = probability
        self._length: int = 0
        for value in values:
            self.insert(value)

    def insert(self, value: Any) -> None:
        """insert a new node in the skip list

        in this implementation the promotions occurs with probability = .5

        Args:
            value (Any): must be comparable
        """
        # reach the right level for the insertion
        node, node_stack = self.root, []
        while node.down:
            # go right until we can't
            while node.next and node.next.value < value:
                node = node.next
            # go down... keep track of the jumps we'll do backtracking
            node_stack.append(node)
            node = node.down
        # this part resembles the search in a normal link list
        while node.next and node.next.value <= value:
            node = node.next
        # special case: no repetitions allowed... do nothing
        if node.value == value:
            return
        # resembles the linked list insertion...
        _ = node.next
        new_node = Node(value)
        node.next = new_node
        new_node.next = _
        # update length
        self._length += 1
        # promote? flip a coin
        while uniform(0, 1) < self.probability:
            if node_stack:
                node = node_stack.pop()
                # resembles linked list insertion, but one level up
                _, node.next = node.next, Node(value)
                # add the links to the new_node downwards
                node.next.next, node.next.down = _, new_node
                # in case we flip a coins again, update new node
                new_node = node.next
            else:
                # promote to new level
                new_head = Node(-float("inf"))
                new_head.next = Node(value)
                new_head.next.down = new_node
                # update the new root
                new_head.down, self.root = self.root, new_head

    def delete(self, value: Any) -> None:
        """delete the node with the given `value`

        Args:
            value (Any): value to delete

        Raises:
            KeyError: raised when not found
        """
        # search
        node = self.root
        while node.down:
            # go right until we can't
            while node.next and node.next.value < value:
                node = node.next
            # special case: trivial erase
            if node.next and node.next.value == value:
                node.next = node.next.next
            # go down...
            node = node.down
        # resembles the linked list search
        while node.next and node.next.value < value:
            node = node.next
        # resembles the linked list deletion
        if node.next and node.next.value == value:
            node.next = node.next.next
            # update length
            self._length -= 1
        else:
            raise KeyError(f"{value} not found")

    def successor(self, value: Any) -> Node:
        """search for a successor of a node with the given value

        Args:
            value (Any): value of the predecessor

        Raises:
            ValueError: raised when there is no successor

        Returns:
            Node: node containing the successor
        """
        # skip search
        node = self.root
        while node.down:
            # go right
            while node.next and node.next.value <= value:
                node = node.next
            # go down...
            node = node.down
        # standard linked list search
        while node:
            if node.value == value:
                if not node.next:
                    raise KeyError(f"{value} not found")
                return node.next
            node = node.next
        raise KeyError(f"{value} not found")

    def search(self, value: Any) -> Node:
        """search for the node cointaining the given `value`

        Args:
            value (Any): `value` to look for

        Raises:
            KeyError: raised when not found

        Returns:
            Node: node containing the given `value`
        """
        # search
        node = self.root
        while node.down:
            # go right until we can't
            while node.next and node.next.value < value:
                node = node.next
            # go down...
            node = node.down
        # resembles linked list search
        while node:
            if node.value == value:
                return node
            node = node.next
        raise KeyError(f"{value} not found")

    def __repr__(self):
        res = []
        current_head = self.root
        level = 0
        while current_head:
            _ = [f"{level}: "]
            node = current_head
            while node:
                # go all the way right
                _.append(f"({node.value})->")
                node = node.next
            res.append("".join(_))
            # next level
            current_head = current_head.down
            level += 1
        return "\n".join(res)

    def __len__(self):
        return self._length
