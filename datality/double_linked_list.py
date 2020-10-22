from typing import Any, Iterable, Optional


class Node:
    """node: chainable storage unit"""

    def __init__(self, value: Any = None):
        self.value: Any = value
        self.next: Optional[Node] = None
        self.prev: Optional[Node] = None


class DoubleLinkedList:
    """implementation of a canonical double linked list

    https://en.wikipedia.org/wiki/Doubly_linked_list
    """

    def __init__(self, values: Iterable[Any] = []):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._length: int = 0
        for value in values:
            self.append(value)

    def append(self, value: Any) -> None:
        """append a new node to the tail of the list

        Args:
            value (Any): value to append, in a new node
        """
        # empty list
        if not self.head:
            self.head = Node(value)
            self.tail = self.head
            self._length += 1
            return
        # general case
        _ = self.tail
        self.tail = Node(value)
        _.next = self.tail
        # update prev links
        self.tail.prev = _
        # update length
        self._length += 1

    def search(self, value: Any) -> Node:
        """search for the first node with the given 'value' and returns it

        Args:
            value (Any): value to be inserted

        Raises:
            ValueError: raised if the value is not found

        Returns:
            Node: Node containing the given `value`
        """
        # empty list
        if not self._length:
            raise ValueError(f"{value} not found")
        # linear search
        node = self.head
        while node:
            if node.value == value:
                return node
            node = node.next
        raise ValueError(f"{value} not found")

    def insert(self, value: Any, index: int) -> None:
        """inserts a new node with the given `value` at the `index` position

        if the given index is out of range the value is inserted at the tail

        Args:
            value (Any): value to be inserted
            index (int): position
        """
        # handle negative indexes
        if index < 0:
            index = self._length + index
        # sanitize
        index = max(index, 0)
        # special index is out of range O(1)
        if self._length < index + 1:
            self.append(value)
            return
        # special case: head O(1)
        if index == 0:
            _ = self.head
            self.head = Node(value)
            self.head.next = _
            # update prev link
            self.head.next.prev = self.head
            # update length
            self._length += 1
            return
        # special case: tail O(1)
        if index + 1 == self._length:
            _ = self.tail
            self.tail = Node(self.tail.value)
            # update prev link
            self.tail.prev = _
            _.value = value
            _.next = self.tail
            # update length
            self._length += 1
            return
        # general case O(n)
        node = self.head
        while node.next and index - 1 > 0:
            node = node.next
            index -= 1
        _ = node.next
        node.next = Node(value)
        node.next.next = _
        # update prev links
        node.next.prev = node
        if node.next.next:
            node.next.next.prev = node.next
        # update length
        self._length += 1

    def delete(self, value: Any) -> None:
        """deletes the node with the given `value`

        Args:
            value (Any): value to be deleted

        Raises:
            ValueError: raised when the value is not found
        """
        # special case: empty list
        if not self.head:
            raise ValueError(f"{value} not in the list")
        # special case: delete head O(1)
        if self.head.value == value:
            # special case: single item
            if self.head == self.tail:
                self.tail = self.head.next
            self.head = self.head.next
            # update links
            if self.head:
                self.head.prev = None
            # update length
            self._length -= 1
            return
        # general case
        node = self.head
        while node.next:
            if node.next.value == value:
                node.next = node.next.next
                # update prev links
                if node.next:
                    node.next.prev = node
                # update length
                self._length -= 1
                return
            node = node.next
        raise ValueError(f"{value} not in the list")

    def __getitem__(self, index: int) -> Node:
        """gets the node at the given `index`

        emulates the behavior of the `[]` operator on a normal list

        Args:
            index (int): get item at this position

        Raises:
            IndexError: raised when the index is out of range

        Returns:
            Node: node at the given `index`
        """
        # handle negative indexes
        if index < 0:
            index = self._length + index
        # sanitize
        index = max(index, 0)
        # special case: empty list
        if not self.head:
            raise IndexError()
        node = self.head
        while node and index > 0:
            node = node.next
            index -= 1
        # out of range?
        if not node:
            raise IndexError()
        return node

    def __repr__(self):
        node = self.head
        _ = []
        while node:
            _.append(f"{node.value}")
            node = node.next
        return " -> ".join(_)

    def __len__(self):
        return self._length
