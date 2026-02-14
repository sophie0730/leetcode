class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start = 0
        current_gas = 0

        for i in range(len(gas)):
            current_gas += gas[i] - cost[i]

            if current_gas < 0:
                current_gas = 0
                start = i + 1

        return start


# 這題的解法在於跟著迴圈去算目前的汽油數量，若小於零，就代表這個index以前出發都不可能繞完一個去
# 所以直接將start 指標指到此index的下一位，再繼續計算
# 只要current_gas都有大於零，就代表可以繼續走下去

# Time Complexity: O(n)
# Space Complexity: O(n)
