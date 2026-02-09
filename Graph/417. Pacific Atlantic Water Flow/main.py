from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # dfs
        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, visited):
            visited.add((r, c))
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and (nr, nc) not in visited
                    and heights[nr][nc] >= heights[r][c]
                ):  # 反向 往高處走
                    dfs(nr, nc, visited)

        for r in range(rows):
            dfs(r, 0, pacific)  # left
            dfs(r, cols - 1, atlantic)  # right

        for c in range(cols):
            dfs(0, c, pacific)  # upper
            dfs(rows - 1, c, atlantic)  # buttom

        return [[r, c] for r, c in pacific & atlantic]  # 取交集
