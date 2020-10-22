from typing import List


class FenwickTree:
    """implementation of the binary indexed tree

    maybe the fastest way to make dynamic range sums queries

    https://en.wikipedia.org/wiki/Fenwick_tree
    """

    def __init__(self, values: List[int] = []):
        # keep track of the original array to compute the deltas, later
        self.original: List[int] = [0] * len(values)
        # we will work with 1 based arrays, so we add an extra 0
        self.tree: List[int] = [0] * (len(values) + 1)
        # build the tree, update all the entries
        for i, value in enumerate(values):
            self.update(i, value)

    def update(self, index: int, value: int):
        """update the `value` of the given `index`

        Args:
            index (int): index position
            value (int): value to update
        """
        delta = value - self.original[index]
        # update the originals
        self.original[index] = value
        # easy bit-wise computations if the indexes start at 1
        index = index + 1
        while index < len(self.tree):
            self.tree[index] += delta
            # go to parent... next power of 2
            index += index & (-index)

    def sum(self, _from: int = 0, _to: int = 0) -> int:
        """get the sum of the range [`_from`: `_to`]

        this works like the **slice notation**, includes the element at `_from`
        but the one at `_to` is not included in the sum.

        if no `_from` is given it sums from 0 to `_to`

        Args:
            _from (int, optional): index where we start the sum. Defaults to 0.
            _to (int, optional): index where we finish the sum. Defaults to 0.

        Raises:
            IndexError: [description]

        Returns:
            int: [description]
        """
        if not 0 <= _from <= _to <= len(self.original):
            raise IndexError(f"{(_from, _to)} out of range")
        # range query
        if _from:
            return self.sum(0, _to) - self.sum(0, _from)
        # accumulate descending in powers of two
        acc = 0
        while _to > 0:
            acc += self.tree[_to]
            _to -= _to & (-_to)
        return acc

    def __repr__(self):
        return repr(self.tree)

    def __len__(self):
        return len(self.original)
