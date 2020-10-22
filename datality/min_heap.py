from typing import Any, Iterable


class Heap:
    """implementation of the min heap

    why **min** insted of **max**? is personal... to me the definition
    of a min heap comes naturally when you think about the real-life heaps

    https://en.wikipedia.org/wiki/Heap_(data_structure)
    """

    def __init__(self, values: Iterable[Any] = []):
        """build the heap from `values` in O(n)

        repairs the heap instead of pushing sequentially

        Args:
            values (Iterable[Any], optional): comparable items. Defaults to [].
        """

        self.core = values
        # repair instead of create! reduces creating time to O(n)
        for i in reversed(range(len(values) // 2)):
            self.sift_down(i)

    def push(self, value: Any) -> None:
        """push a new node with the `value` into the heap

        Args:
            value (Any): value to push into the heap, needs to be comparable
        """
        # self.core is a long name to write...
        core = self.core
        # append new value to the tail
        i = len(core)
        core.append(value)
        # auxiliar function to compute the parent index

        def parent(i):
            return max((i - 1) // 2, 0)

        # bubble up...
        while core[parent(i)] > core[i]:
            core[parent(i)], core[i] = core[i], core[parent(i)]
            i = parent(i)

    def peek(self) -> Any:
        """get the minimum value of the heap in O(1)

        Raises:
            IndexError: raised when the heap is empty

        Returns:
            Any: min value at the top of the heap
        """
        # special case: empty heap
        if not self.core:
            raise IndexError("peek() on empty heap...")
        return self.core[0]

    def sift_down(self, index: int = 0) -> None:
        """bubble down a value until the heap property is preserved

        Args:
            index (int, optional): index to start sifting from. Defaults to 0.
        """
        if not 0 <= index < len(self.core):
            return
        core = self.core

        def left():
            """get the index of the left child"""
            return index * 2 + 1 if index * 2 + 1 < len(core) else False

        def right():
            """get the index of the right child"""
            return index * 2 + 2 if index * 2 + 2 < len(core) else False

        # bubble down...
        while (left() and core[left()] < core[index]) or (
            right() and core[right()] < core[index]
        ):
            max_child = left()
            if right() and core[right()] < core[left()]:
                max_child = right()
            # swap parent with the bigger child
            core[index], core[max_child] = core[max_child], core[index]
            # update index
            index = max_child

    def pop(self) -> Any:
        """pops the maximun/minimum in O(1)

        Raises:
            IndexError: raised when the heap is empty

        Returns:
            Any: the `value` at the top of the heap
        """
        self.core
        # special case: empty heap
        if not self.core:
            raise IndexError("pop() on empty heap...")
        # swap min <-> tail
        self.core[0], self.core[-1] = self.core[-1], self.core[0]
        minimum = self.core.pop()
        # bubble down
        self.sift_down()
        return minimum

    def __len__(self):
        return len(self.core)

    def __repr__(self):
        return repr(self.core)
