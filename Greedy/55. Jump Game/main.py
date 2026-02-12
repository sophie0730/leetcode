class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            # if this position add the max step can reach goal, means it is possible to reach
            if i + nums[i] >= goal:
                goal = i  # backward, testing if we can reach the previous position

        return goal == 0


# Time Complexity: O(n)
# Space Complexity: O(1)
