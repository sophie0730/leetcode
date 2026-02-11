from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # 每個節點的根節點都設為自己
        parent = [i for i in range(len(edges) + 1)]

        def find(x):
            # 沿著 parent往上追溯，直到找到一個節點的parent是自己，那就是根節點
            if parent[x] != x:
                # 把沿路節點都指向根節點（扁平化，讓下次查詢更快O(n) -> O(1))
                parent[x] = find(parent[x])

            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x == root_y:
                return False

            # 把root_x的parent設為root y，把x的根節點放在y下面。因為最終的根節點一定是同一個，合併之後find會沿著同個路徑追到同一個根
            parent[root_x] = root_y
            return True

        for u, v in edges:
            # 兩者的根節點相同，若再連結就會形成環，變成冗余邊
            if not union(u, v):
                return [u, v]

        return []
