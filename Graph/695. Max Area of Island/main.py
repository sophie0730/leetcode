# Find the max area -> dfs


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        max_island = 0
        visited = set()

        def dfs(r, c):
            if (
                r not in range(row)
                or c not in range(col)
                or (r, c) in visited
                or grid[r][c] == 0
            ):
                return 0

            visited.add((r, c))

            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        for r in range(row):
            for c in range(col):
                if (r, c) not in visited and grid[r][c] == 1:
                    max_island = max(max_island, dfs(r, c))

        return max_island


# Time Complexity: O(m x n) m=rows n=cols
