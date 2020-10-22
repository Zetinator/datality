from typing import List, Optional


class Node:
    """node chainable storage unit"""

    def __init__(self, value: Optional[float] = None):
        self.min = self.max = self.sum = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


class SegmentTree:
    """implementation of the segment tree (min/max/sum range query)

    https://en.wikipedia.org/wiki/Segment_tree
    """

    def __init__(self, nums: List[float] = []):
        self.nums = nums
        self.root: Optional[Node] = None
        if not self.nums:
            return

        def insert(l: int = 0, r: int = len(self.nums) - 1):
            """insert the nodes recursively

            this kinda resembles like merge-sort innit? :D
            """
            # base case: just one element left in the given interval
            if l == r:
                return Node(self.nums[l])
            # divide
            m = (l + r) // 2
            node = Node()
            node.left, node.right = insert(l, m), insert(m + 1, r)
            # conquer
            node.min = min(node.left.min, node.right.min)
            node.max = max(node.left.max, node.right.max)
            node.sum = sum([node.left.sum, node.right.sum])
            return node

        self.root = insert()

    def query_min(self, _from: int, _to: int) -> float:
        """return the min value in the given range (`_from`, `_to`) O(log(N))

        analog to the slice notation [`_from` : `_to`]

        Args:
            _from (int): start of the range
            _to (int): end of the range

        Raises:
            ValueError: raised when empty or invalid range

        Returns:
            float: min range query
        """
        # special case: empty tree
        if not self.root:
            raise ValueError(f"query on empty tree")
        # special case: invalid range as input
        if not 0 <= _from < _to <= len(self.nums):
            raise ValueError(f"invalid range: {(_from,_to)}")

        def query(
            node: Node = self.root,
            l: int = 0,
            r: int = len(self.nums) - 1,
            _from: int = _from,
            _to: int = _to - 1,
        ) -> float:
            """binary search with ranges

            when the inner pointers fit inside the outer's we are done...

            Args:
                node (Node, optional): current node. Defaults to self.root.
                l (int, optional): inner left. Defaults to 0.
                r (int, optional): inner right. Defaults to len(self.nums)-1.
                _from (int, optional): outer left. Defaults to 0.
                _to (int, optional): outer right. Defaults to len(self.nums)-1.

            Returns:
                float: [description]
            """
            # avoid invalid ranges...
            if l > r or r < _from or _to < l:
                return float("inf")
            # base condition: the inner fits inside the outer
            if _from <= l <= r <= _to:
                return node.min
            # keep exploring
            m = (l + r) // 2
            return min(
                query(node.left, l, m, max(l, _from), min(m, _to)),
                query(node.right, m + 1, r, max(m + 1, _from), min(r, _to)),
            )

        return query()

    def query_sum(self, _from: int, _to: int) -> float:
        """return the sum value in the given range (`_from`, `_to`) O(log(N))

        analog to the slice notation [`_from` : `_to`]

        Args:
            _from (int): start of the range
            _to (int): end of the range

        Raises:
            ValueError: raised when empty or invalid range

        Returns:
            float: sum range query
        """
        # special case: empty tree
        if not self.root:
            raise ValueError(f"query on empty tree")
        # special case: invalid range as input
        if not 0 <= _from < _to <= len(self.nums):
            raise ValueError(f"invalid range: {(_from,_to)}")

        def query(
            node: Node = self.root,
            l: int = 0,
            r: int = len(self.nums) - 1,
            _from: int = _from,
            _to: int = _to - 1,
        ) -> float:
            """binary search with ranges

            when the inner pointers fit inside the outer's we are done...

            Args:
                node (Node, optional): current node. Defaults to self.root.
                l (int, optional): inner left. Defaults to 0.
                r (int, optional): inner right. Defaults to len(self.nums)-1.
                _from (int, optional): outer left. Defaults to 0.
                _to (int, optional): outer right. Defaults to len(self.nums)-1.

            Returns:
                float: [description]
            """
            # avoid invalid ranges...
            if l > r or r < _from or _to < l:
                return 0
            # base condition: the inner fits inside the outer
            if _from <= l <= r <= _to:
                return node.sum
            # keep exploring
            m = (l + r) // 2
            return sum(
                [
                    query(node.left, l, m, max(l, _from), min(m, _to)),
                    query(node.right, m + 1, r, max(m + 1, _from), min(r, _to)),
                ]
            )

        return query()

    def query_max(self, _from: int, _to: int) -> float:
        """return the max value in the given range (`_from`, `_to`) O(log(N))

        analog to the slice notation [`_from` : `_to`]

        Args:
            _from (int): start of the range
            _to (int): end of the range

        Raises:
            ValueError: raised when empty or invalid range

        Returns:
            float: max range query
        """
        # special case: empty tree
        if not self.root:
            raise ValueError(f"query on empty tree")
        # special case: invalid range as input
        if not 0 <= _from < _to <= len(self.nums):
            raise ValueError(f"invalid range: {(_from,_to)}")

        def query(
            node: Node = self.root,
            l: int = 0,
            r: int = len(self.nums) - 1,
            _from: int = _from,
            _to: int = _to - 1,
        ) -> float:
            """binary search with ranges

            when the inner pointers fit inside the outer's we are done...

            Args:
                node (Node, optional): current node. Defaults to self.root.
                l (int, optional): inner left. Defaults to 0.
                r (int, optional): inner right. Defaults to len(self.nums)-1.
                _from (int, optional): outer left. Defaults to 0.
                _to (int, optional): outer right. Defaults to len(self.nums)-1.

            Returns:
                float: [description]
            """
            # avoid invalid ranges...
            if l > r or r < _from or _to < l:
                return -float("inf")
            # base condition: the inner fits inside the outer
            if _from <= l <= r <= _to:
                return node.max
            # keep exploring
            m = (l + r) // 2
            return max(
                query(node.left, l, m, max(l, _from), min(m, _to)),
                query(node.right, m + 1, r, max(m + 1, _from), min(r, _to)),
            )

        return query()

    def __repr__(self):
        res = []

        def _r(
            node: Node = self.root,
            l: int = 0,
            r: int = len(self.nums) - 1,
            level: int = 0,
        ) -> None:
            """inorder traversal"""
            if not node:
                return
            m = (l + r) // 2
            _r(node.right, m + 1, r, level + 1)
            res.append("\t" * level + f"-->{(node.max, node.min, node.sum)}{[l, r]}")
            _r(node.left, l, m, level + 1)

        _r()
        return "\n".join(res)

    def __len__(self):
        return len(self.nums)
