import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = nums[:k]
        heapq.heapify(min_heap)

        for num in nums[k:]:
            # min heap 只確保root是最小的，如果要找第k大，就是維持一個k size的min heap，如果遇到比root大的就把root換掉
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)
        
        return min_heap[0]