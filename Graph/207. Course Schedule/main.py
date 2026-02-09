class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = defaultdict(list)
        taken = set()

        for course, p in prerequisites:
            pre[course].append(p)  # 每個prerequisite都長出一個邊 每個邊之後都會被訪問

        def dfs(course):
            if not pre[course]:
                return True

            if course in taken:
                return False

            taken.add(course)

            for p in pre[course]:
                if not dfs(p):
                    return False

            taken.remove(course)
            pre[course] = []  # 之後如果再走到這個節點，會直接回傳True, 不會重新visit
            return True

        # course number: 0, 1, 2, ...,to prevent no dependency courses
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
