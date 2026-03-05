# 最短路徑 -> Dijkstra's Algorithm
#
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for src, dst, cost in times:
            graph[src].append((dst, cost))

        queue = [(0, k)]  # cost, started node
        visited = set()
        max_cost = 0

        while queue:
            cost, node = heapq.heappopleft(
                queue
            )  # 自動找到cost最小的set並拿出 符合Dijkstra的要求-找最短路徑ㄙ

            if node in visited:
                continue

            max_cost = max(cost, max_cost)
            neighbours = graph[node]

            for neighbour in neighbours:
                new_node, new_cost = neighbour

                if new_node not in visited:
                    curr_cost = cost + new_cost
                    heapq.heappush(queue, (curr_cost, new_cost))

        return max_cost if len(visited) == n else -1


# Time Coplexity(O(N + V logN)), v=veticles, n=nodes
# 插入最小堆積時，最壞情況下堆積裡面有n個set, 因為插入時會一個一個往上比對是否有比父節點大 所以複雜度是log n
# 再來遍歷每個邊，所以每個邊都會執行插入堆疊 複雜度變V log N
# 再來我們要初始化每個節點，每個節點都要走過，所以再加一個Ｎ
