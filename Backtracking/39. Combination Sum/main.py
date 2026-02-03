class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def make_combine(i, combination, total):
            if total == target:
                res.append(combination[:])
                return
            
            if total > target or i >= len(candidates):
                return

            combination.append(candidates[i])
            make_combine(i, combination, total+candidates[i])

            combination.pop()
            make_combine(i+1, combination, total) # pop this number and try the next

        make_combine(0, [], 0) #initialization
        return res


# Decision Tree Example for candidates = [2,3,7], target = 7

        #               []
        #             /   \
        #          [2]     []
        #         /   \      \
        #      [2,2]   [2]    [3]
        #     /   \       \     \
        # [2,2,2]  [2,2,3]  [3,3] [7]

# Time: O(2^n) we have two choices for each candidate: include it or not include it.
# O(t/d), where t is the target and d is the smallest candidate, representing the depth of the recursion.