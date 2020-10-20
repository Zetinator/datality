from typing import Any, Dict, List, Optional


class Node:
    """node chainable storage unit"""

    def __init__(self, value: Any = None):
        self.value = value
        self.children: Dict[Any, Any] = {}


class Trie:
    """implementation of the Trie

    https://en.wikipedia.org/wiki/Trie
    """

    def __init__(self, keys: List[Any] = []):
        self.root: Optional[Node] = Node()
        self.length: int = 0
        for key in keys:
            self.insert(key)

    def insert(self, key: Any) -> None:
        """insert the give `key` in the trie

        Args:
            key (Any): the key to insert (must be iterable)
        """
        node = self.root
        for e in key:
            if e not in node.children:
                node.children[e] = Node()
            node = node.children[e]
        if node.value is not None:
            # we are not actually inserting a new node
            self.length -= 1
        node.value = key
        # update length
        self.length += 1

    def delete(self, key: Any) -> None:
        if not key:
            raise KeyError(f"{key} not found")

        def r(node: Node, partial_key: Any = key) -> bool:
            """recursively search and destroy :D"""
            # found... remove the value
            if key == node.value:
                node.value = None
                # propagate the deletion returning true as signal
                if not node.children:
                    return True
                else:
                    return False
            # keep exploring
            if partial_key[0] in node.children:
                # when we receive the *signal* cut off the lineage
                if r(node.children[partial_key[0]], partial_key[1:]):
                    del node.children[partial_key[0]]
                    # chain reaction?
                    if node.value is None and not node.children:
                        return True
                    else:
                        return
            else:
                raise KeyError(f"{key} not found")

        r(self.root)
        # update length
        self.length -= 1

    def predict(self, partial_key: Any) -> List[Any]:
        """given a partial key find all the possible keys inside the trie

        Args:
            partial_key (Any): key must be iterable

        Returns:
            List[Any]: list with the predictions
        """
        tmp = []
        # explore as far as we can
        node = self.root
        for e in partial_key:
            if e in node.children:
                node = node.children[e]
            else:
                return []

        def deep(node: Node):
            """explore all leafs from where we currently are"""
            # found a match, add it
            if node.value is not None:
                tmp.append(node.value)
            # keep exploring
            for child in node.children.values():
                deep(child)

        deep(node)
        return tmp

    def search(self, key: Any) -> Node:
        """searches for the node with the given `key` in the trie

        Args:
            key (Any): the key must be iterable

        Raises:
            KeyError: raised when not found

        Returns:
            Node: the node containing the given `key`
        """
        node = self.root
        for e in key:
            if e not in node.children:
                raise KeyError(f"{key} not found")
            node = node.children[e]
        return node

    def __repr__(self):
        res = []

        def r(node: Node, level: int = 0):
            # print under line
            if node.value is not None:
                res.append("\n" + " " * 4 * level + f"{node.value}\n")
                # remember where we are to keep printing children
                if node.children:
                    res.append(" " * 4 * level)
            # explore the children
            children = list(node.children.items())
            for i, (k, child) in enumerate(children):
                res.append(f"-({k})")
                r(child, level + 1)
                if i < len(children) - 1:
                    res.append(" " * 4 * level)

        r(self.root)
        return "".join(res)

    def __len__(self):
        return self.length
