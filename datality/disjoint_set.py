from typing import Any, Dict


class DJS:
    """implementation of Tarjan's disjoint sets

    https://en.wikipedia.org/wiki/Disjoint-set_data_structure
    """

    def __init__(self):
        self.parents: Dict[Any, Any] = dict()

    def find(self, node: Any) -> Any:
        """get the representative node of this node

        Args:
            node (Any): node to look the representantive for

        Returns:
            Any: the representantive of this node
        """
        # path compression
        if self.parents.get(node, node) != node:
            self.parents[node] = self.find(self.parents[node])
        return self.parents.get(node, node)

    def same(self, node_1: Any, node_2: Any) -> bool:
        """check if the 2 nodes have the same representantive

        if the roots are the same, they are in the same set

        Args:
            node_1 (Any): first node
            node_2 (Any): second node

        Returns:
            bool: True if both belong to the same set
        """
        return self.find(node_1) == self.find(node_2)

    def union(self, node_1: Any, node_2: Any) -> None:
        """join the 2 nodes inside the same set

        Args:
            node_1 (Any): first node
            node_2 (Any): second node
        """
        root_1, root_2 = self.find(node_1), self.find(node_2)
        # same set already?
        if root_1 == root_2:
            return
        # join the nodes, the tiny inside the bigger
        if node_1 == root_1:
            self.parents[root_1] = root_2
        else:
            self.parents[root_2] = root_1

    def __repr__(self):
        return repr(self.parents)

    def __len__(self):
        return len(self.parents)
