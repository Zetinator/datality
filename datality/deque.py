from typing import Any, Iterable, Optional

from datality.double_linked_list import DoubleLinkedList


class Node:
    """node chainable storage unit"""

    def __init__(self, value: Any = None):
        self.value: Any = value
        self.next: Optional[Node] = None


class Deque(DoubleLinkedList):
    """implementation of a double ended queue

    https://en.wikipedia.org/wiki/Double-ended_queue
    """

    def __init__(self, values: Iterable[Any] = []):
        super().__init__(values)

    def append_left(self, value: Any) -> None:
        """append a new node to the head of the list

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
        _ = self.head
        self.head = Node(value)
        self.head.next = _
        # update length
        self._length += 1

    def pop_left(self) -> Any:
        """pop the element at the begining of the list

        Returns:
            Any: the element at the begining of the list
        """
        # special case: empty list
        if not self.head:
            raise IndexError()
        _ = self.head
        # special case: single item
        if self.head == self.tail:
            self.tail = self.head.next
        self.head = self.head.next
        return _

    def pop_right(self) -> Any:
        """pop the element at the end of the list

        Returns:
            Any: the element at the end of the list
        """
        # special case: empty list
        if not self.head:
            raise IndexError()
        _ = self.tail
        # special case: single item
        if self.head == self.tail:
            self.head = None
        self.tail = self.tail.prev
        return _
