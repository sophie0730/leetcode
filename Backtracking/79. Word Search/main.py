class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(row, col, i):
            if i == len(word):
                return True
            if (
                row < 0
                or row >= rows
                or col < 0
                or col >= cols
                or board[row][col] != word[i]
            ):
                return False

            temp = board[row][col]
            board[row][col] = "#"

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if dfs(row + dr, col + dc, i + 1):
                    return True

            board[row][col] = temp
            return False

        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True

        return False


# Time Complexity: O(m*n*4^l) l=word長度，4是因為要探索四個方向
# Space Complexity: O(l) word的長度就等於遞迴的深度
