class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def create_subset(i):
            if i == len(nums):
                res.append(subset[:])
                return
            
            subset.append(nums[i])
            create_subset(i+1)
            print(subset)

            subset.pop()
            create_subset(i+1)
            print(subset)
        
        create_subset(0)
        return res
    
# Time: O(2^N) 陣列中的每個數字都有選和不選兩種可能