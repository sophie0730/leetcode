class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            
            if complement in numMap: # the key of numMap is values
                return [numMap[complement], i]
            
            numMap[nums[i]] = i

        return []

