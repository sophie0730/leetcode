# the max speed is koko eats max(piles) bananas each hour
# the min speed is eating 1 banana each hour
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(k):
            hours = 0
            for pile in piles:
                hours += (pile + k - 1) // k

            return hours <= k
        
        left, right = 1, max(piles)
        result = right

        while left <= right:
            mid = (left + right) // 2

            if can_finish(mid):
                # keep find the min speed
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return result

