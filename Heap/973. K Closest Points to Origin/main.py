import heapq
from typing import List 

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) == k:
            return points

        heap = []

        for (x, y) in points:
            distance = (x*x + y*y)
            if len(heap) == k:
                heapq.heappushpop_max(heap, (distance, x, y))
            else:
                heapq.heappush_max(heap, (distance, x, y))

        return [(x, y) for (distance, x, y) in heap]
