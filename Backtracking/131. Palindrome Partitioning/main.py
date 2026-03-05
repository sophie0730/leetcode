class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def is_palindrome(sub):
            return sub == sub[::-1]

        def backtrack(start, path):
            if start == len(s):
                result.append(path[::])
                return

            for end in range(start + 1, len(s) + 1):
                if is_palindrome(s[start:end]):
                    backtrack(end, path + [s[start:end]])

        backtrack(0, [])
        return result


# Time Complexity: O(n * 2^n) 2^n是遞迴的時間複雜度（字串n長度，有n-1個切割地方，每個地方可以選擇切或不切）
# ，n是每次遞迴會複製原字串的時間
# Space Complexity: O(n) 最多存n個子字串 每個子字串長度為1
