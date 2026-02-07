# use dfs and hash map
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def __init__(self):
        self.clone_nodes = {}  # to record the copied node

    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if node is None:
            return None

        if node in self.clone_nodes:
            return self.clone_nodes[node]

        clone = Node(node.val)
        self.clone_nodes[node] = clone

        for neighbor in node.neighbors:  # we should record not only the node but also the neighbors (the connection between nodes)
            clone.neighbors.append(self.cloneGraph(neighbor))

        return clone


# Time Complexity: O(V + E) v=訪問節點的數量 E=每條邊訪問一遍
