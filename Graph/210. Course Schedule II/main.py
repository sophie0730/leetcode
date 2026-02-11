from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [
            [] for _ in range(numCourses)
        ]  # create an empty graph for all possible courses
        in_degree = [0] * numCourses

        result = []

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)  # 當完成這門課後 可以解鎖哪些課程
            in_degree[course] += 1  # 課程的解鎖條件+1

        # 不必先修的課程加入queue
        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        while queue:
            course = queue.pop()
            result.append(course)

            for next_course in graph[course]:
                # next_course是course的先修課程，解鎖一個條件
                in_degree[next_course] -= 1

                # 條件都被解鎖，等於不必再有先修課程，加入queue
                if in_degree[next_course] == 0:
                    # 加入queue後，下一次跑while 回圈時，加入result
                    queue.append(next_course)

        return result if len(result) == numCourses else []


# Time Complexity: O(V+E) V Vertices 節點：課程 E Egde: 先修關係。每個節點和邊都只訪問一次
# Space Complexity: O(V+E) Graph. result和in_degree都是O(V) -> 儲存節點
