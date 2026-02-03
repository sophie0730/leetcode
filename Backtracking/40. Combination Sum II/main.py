class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(target, start, comb):
            if target < 0:
                return
            if target == 0:
                res.append(comb)
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]: # skip duplicates
                    continue
                if candidates[i] > target:
                    break
                
                dfs(target-candidates[i], i+1, comb+[candidates[i]]) # we should find the remain target

        dfs(target, 0, [])
        return res
    
# candidates = [10,1,2,7,6,1,5], target = 8
# 排序後: [1,1,2,5,6,7,10]

#          dfs(8, 0, [])
#          /    |    \
#     [1]     [1]   [2]...
#     (8-1)    ❌   (跳過重複)
#       |      跳過
#    dfs(7,1,[1])
#     /    |    \
#  [1,1] [1,2] [1,5]...
#  (6)   (5)   (2)
#   |     |     |
#  [1,1,6] ✓  [1,2,5] ✓  [1,7] ✓