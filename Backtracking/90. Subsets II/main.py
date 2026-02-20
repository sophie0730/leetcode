class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()  # 避免產生重複的子集合

        def create_subset(i):
            if i == len(nums):
                res.append(subset[:])
                return

            subset.append(nums[i])
            create_subset(i + 1)  # 繼續往下加的路徑

            subset.pop()  # 不加上這個element的路徑

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                # 重複數字的情況
                i += 1  # skip

            create_subset(i + 1)  # 繼續走不加上element的路徑

        create_subset(0)
        return res


# Time Complexity: O(2^n) n = array length
# space complexity: O(n) or O(2^n)(包含所有使用過的儲存空間)
