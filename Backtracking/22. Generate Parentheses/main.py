class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(left, right, s):
            if len(s) == n * 2:
                res.append(s)
                return

            if left < n:
                dfs(left + 1, right, "(")

            if right < left:
                dfs(left, right + 1, ")")

        dfs(0, 0, "")
        return res


# Time Complexity: O(2*(2^n)) = O(4^n) 有2n長的字串 每個空位都可以填入左括號或者右括號
# Space Complexity: O(2^n) n層 ＊ n長度的字串
