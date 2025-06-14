class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        old = image[sr][sc]
        if old == color:
            return image
        m = len(image)
        n = len(image[0])

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or image[i][j] != old:
                return
            
            image[i][j] == color

            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        dfs(sr, sc)
        return image


