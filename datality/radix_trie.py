from typing import Any, Dict, Iterable


class Node:
    """node chainable storage unit"""

    def __init__(self, value: Any = None):
        self.value: Any = value
        self.children: Dict[Any, Any] = {}


class RadixTree:
    """implementation of the Radix Tree

    https://en.wikipedia.org/wiki/Radix_tree
    """

    def __init__(self, keys: Iterable[Any] = []):
        self.root: Node = Node()
        self._length: int = 0
        for key in keys:
            self.insert(key)

    def insert(self, key: Any) -> None:
        """insert the given `key` in the radix tree

        Args:
            key (Any): the key must be iterable
        """

        def lcp(key_1: Any, key_2: Any) -> int:
            """largest common prefix"""
            i = 0
            for i in range(min(len(key_1), len(key_2))):
                if key_1[i] != key_2[i]:
                    return i
            return i + 1

        def r(node: Node, partial_key: Any) -> None:
            """recursive branching

            just follow the rules...
            1. no children -> new branch
            2. common root + remainings -> split and extend
            3. common root + no remainings -> extend
            4. no common root -> create new branch

            Args:
                node (Node): current node
                partial_key (Any): partial segment of the key
            """
            # special case 1: no children
            if not node.children:
                node.children.setdefault(partial_key, Node()).value = key
                # update length
                self._length += 1
                return
            # look for similar roots in the children...
            for k, child in node.children.items():
                i = lcp(k, partial_key)
                prefix, suffix, partial_key = k[:i], k[i:], partial_key[i:]
                if prefix and suffix:
                    # special case 2: split and extend
                    node.children[prefix] = Node()
                    del node.children[k]
                    # append suffixs to common root
                    node.children[prefix].children[suffix] = Node()
                    new_child = node.children[prefix].children[suffix]
                    new_child.value = child.value
                    new_child.children = child.children
                    return r(node.children[prefix], partial_key)
                elif prefix and not suffix:
                    # special case 3: common root found... extending
                    return r(child, partial_key)
            # special case 4: no common root... create new child branch
            node.children.setdefault(partial_key, Node()).value = key
            # update length
            self._length += 1

        return r(self.root, key)

    def predict(self, partial_key: Any = None) -> []:
        """predict all branches of the lowest common ancestor

        Args:
            partial_key (Any, optional): must be iterable. Defaults to None.

        Returns:
            []: [description]
        """
        if not self.root.children:
            return []

        def lcp(key_1, key_2):
            """largest common prefix"""
            i = 0
            while i < min(len(key_1), len(key_2)):
                if key_1[i] != key_2[i]:
                    return i
                i += 1
            return i

        res = []

        def dig(node: Node) -> None:
            """explore all the leafs from the node"""
            if node.value is not None:
                res.append(f"{node.value}")
            for k, child in node.children.items():
                dig(child)

        def r(node: Node, partial_key: Any) -> None:
            """search recursively the given partial_key"""
            # look for similar roots in the children...
            for k, child in node.children.items():
                i = lcp(k, partial_key)
                prefix, _, partial_key = k[:i], k[i:], partial_key[i:]
                if prefix in node.children:
                    # recurse on the shared root
                    return r(node.children[prefix], partial_key)
            return dig(node)

        r(self.root, partial_key)
        return res

    def search(self, key: Any) -> Node:
        """search for a given `key` in the trie

        Args:
            key (Any): key must be iterable

        Raises:
            KeyError: raised when not found

        Returns:
            Node: node containing the given `key`
        """
        if not self.root.children:
            raise KeyError(f"{key} not found")

        def lcp(key_1: Any, key_2: Any) -> int:
            """largest common prefix"""
            i = 0
            while i < min(len(key_1), len(key_2)):
                if key_1[i] != key_2[i]:
                    return i
                i += 1
            return i

        _key = key[:]

        def r(node: Node, key: Any) -> Node:
            """search recursively the node with the given key"""
            if not key:
                return node
            # look for similar roots in the children...
            for k, child in node.children.items():
                i = lcp(k, key)
                prefix, _, key = k[:i], k[i:], key[i:]
                if prefix:
                    # recurse on the shared root
                    return r(node.children[prefix], key)
            raise KeyError(f"{_key} not found")

        return r(self.root, key)

    def __repr__(self):
        res = []

        def r(node, level):
            if node.value is not None:
                res.append("\t" * (level - 1) + f"({node.value})\n")
            for k, child in node.children.items():
                res.append("\t" * level + f"--<{k}>--\n")
                r(child, level + 1)

        r(self.root, 0)
        return "".join(res)

    def __len__(self):
        return self._length
