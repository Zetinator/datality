from typing import List, Optional


class Node:
    """node chainable storage unit

    each node has the same basic structure: u, min, max, summary, clusters
    """

    def __init__(self, u: int):
        self._u = 2
        self.min = self.max = None
        self.clusters = {}
        self.summary = None
        # find the size of this universe (next power of 2 containing all the keys)
        while self._u < u:
            self._u = self._u << 1

    def __repr__(self):
        return f"{(self.min, self.max)}u{self._u}"


class VEB:
    """implementation of the van emde boas tree

    this one uses hash tables to achive `O(n*log(log(U)))` space efficiency, instead of the original `O(U)`
    where: `n` is the number of elements in the tree, and `U` is the size of the `universe`

    https://en.wikipedia.org/wiki/Van_Emde_Boas_tree
    https://www.youtube.com/watch?v=hmReJCupbNU&t=1838s

    the ADT contains the following methods:
        - insert: insert a new node in the tree in O(lg lg u)
        - search: return the node with the given value in O(lg lg u)
        - min: return the min element in O(1)
        - max: returns the max element in O(1)
        - delete: delete the given value from the tree in O(lg lg U)
        - successor: return the next in order successor in O(lg lg U)

    usage example:
        # from a list of keys
        v = VEB([33, 66, 1, 65, 5, 7, 41])
        # set universe size
        v = VEB(u=16, keys=[1,3,5,11])
    """

    def __init__(self, keys: List[int] = [], u: Optional[int] = None):
        if u is not None and not 2 <= u:
            raise ValueError(f"{u} must be greater or equal than 2")
        # find the size of universe (next power of 2 containing all the keys)
        self._u = 2
        maximum = u or max(keys, default=2)
        # choose ideal size of the universe
        while self._u < maximum:
            self._u = self._u << 1
        # double it once more for safety
        self._u = self._u << 1
        # build tree from root
        self.root: Node = Node(self._u)
        # insert elements in the tree
        for key in keys:
            self.insert(key)

    def min(self) -> int:
        """returns the min in the tree O(1)

        Returns:
            int: current min in the tree
        """
        if self.root.min is None:
            raise IndexError("empty tree")
        return self.root.min

    def max(self) -> int:
        """returns the max in the tree O(1)

        Returns:
            int: current max in the tree
        """
        if self.root.min is None:
            raise IndexError("empty tree")
        return self.root.max

    def search(self, key: int) -> bool:
        """find a given `key` in the tree O(log log u)

        Args:
            key (int): key to look for

        Raises:
            KeyError: raised when not found

        Returns:
            bool: if the key is contained
        """
        # search recursively
        def r(node, x):
            if node.min == x or node.max == x:
                return True
            # get cluster -> i (high) and offset -> j (low)
            i = x // int(node._u ** (1 / 2))
            j = x % int(node._u ** (1 / 2))
            # don't give up... keep looking!
            if i in node.clusters:
                return r(node.clusters[i], j)
            return False

        res = r(self.root, key)
        if not res:
            raise KeyError(f"{key} not found")
        return res

    def insert(self, key: int) -> None:
        """insert a new key in O(log log u)

        Args:
            key (int): `key` to be inserted

        Raises:
            ValueError: raised for invalid keys...
        """
        if not 0 <= key < self._u:
            raise ValueError(f"{key} out of the universe")

        def r(node, partial_key: int) -> None:
            """insert recursively"""
            # pseudo lazy propagation, makes the insertion log(log(U))
            if node.min is None:
                node.min = node.max = partial_key
                return
            if partial_key < node.min:
                partial_key, node.min = node.min, partial_key
            if partial_key > node.max:
                node.max = partial_key
            # get cluster -> i (high) and offset -> j (low)
            i = partial_key // int(node._u ** (1 / 2))
            j = partial_key % int(node._u ** (1 / 2))
            u = int(node._u ** (1 / 2))
            # update summary if the corresponding cluster was empty
            if node._u > 2 and i not in node.clusters:
                if not node.summary:
                    node.summary = Node(u)
                r(node.summary, i)
            # update the corresponding cluster
            if node._u > 2:
                r(node.clusters.setdefault(i, Node(u)), j)

        r(self.root, key)

    def successor(self, key: int) -> int:
        """returns the successor of the given key in the tree

        the classic data structure returns the size of the universe `self._u`
        if the successor is not found... we will raise an exception

        Args:
            key (int): key of the predecessor

        Raises:
            KeyError: raised when the successor is not in the tree

        Returns:
            int: the key of the sucessor
        """
        if self.root.min is None:
            raise KeyError(f"successor of {key} not found")

        def r(node, x):
            # trivial case
            if x < node.min:
                return node.min
            # no successor availible...
            if x >= node.max:
                return node._u
            # get cluster -> i (high) and offset -> j (low)
            i = x // int(node._u ** (1 / 2))
            j = x % int(node._u ** (1 / 2))
            # professor Erik Demaine was missing this next line...
            if not node._u > 2 and x < node.max:
                return node.max
            if node._u > 2 and i in node.clusters and j < node.clusters[i].max:
                # if key < max in the cluster for sure the successor can be found here
                j = r(node.clusters[i], j)
            else:
                # take a look in the summary first
                i = r(node.summary, i)
                j = node.clusters[i].min
            return i * int(node._u ** (1 / 2)) + j

        res = r(self.root, key)
        if res == self._u:
            raise KeyError(f"successor of {key} not found")
        return res

    def delete(self, key: int) -> None:
        """deletes a `key` from the tree in O(log log U)"""
        # special case: empty tree
        if self.root.min is None:
            return

        def r(node, x: int) -> bool:
            """delete recursively"""
            # base case: we reached a node with a single element
            # return a signal to the parent to erase this empty child
            if node.min is None or x < node.min or node.max < x:
                return False
            if node.min == node.max:
                return True
            # special case: erasing min
            if x == node.min:
                # we dont want to recurse into a node with no summary...
                if not node._u > 2:
                    node.min = node.max
                    return False
                tmp = node.summary.min
                # new min discovered, update
                x = node.min = tmp * int(node._u ** (1 / 2)) + node.clusters.get(tmp, Node(2)).min or 0
            # get cluster -> i (high) and offset -> j (low)
            i = x // int(node._u ** (1 / 2))
            j = x % int(node._u ** (1 / 2))
            # simetrical with respect to insert, we delete first
            if node._u > 2 and i in node.clusters:
                if r(node.clusters[i], j):
                    del node.clusters[i]
            # then if is the cluster is empty, update the summary
            if node._u > 2 and i not in node.clusters:
                r(node.summary, i)
            # special case: erasing max, very similar to the min case
            if x == node.max:
                if not node.clusters:
                    node.max = node.min
                    node.summary = None
                    return
                tmp = node.summary.max
                if tmp in node.clusters:
                    node.max = tmp * int(node._u ** (1 / 2)) + node.clusters.get(tmp, Node(2)).max or 0
            return False

        # base case: we reached a node with a single element
        # return a signal to the parent to erase this empty child
        if r(self.root, key):
            self.root = Node(self._u)

    def __repr__(self):
        """prints first the main node and summary trees recursevly"""
        main, summary = [], []

        def r(tmp, node, level=0):
            if not node:
                return
            tmp.append("\t" * level + f"-->{node}")
            for cluster in node.clusters.values():
                r(tmp, cluster, level + 1)

        # recurse on both the main and the summary tree
        r(main, self.root)
        r(summary, self.root.summary)
        main, summary = "\n".join(main), "\n".join(summary)
        return f"main:\n{main}\nsummary:\n{summary}"

    def __len__(self):
        return self._u
