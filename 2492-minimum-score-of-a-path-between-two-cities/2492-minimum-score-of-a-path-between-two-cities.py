from typing import List

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n + 1)]

        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))

        visited = [False] * (n + 1)
        ans = float("inf")

        def dfs(node):
            nonlocal ans
            visited[node] = True

            for nei, w in graph[node]:
                ans = min(ans, w)
                if not visited[nei]:
                    dfs(nei)

        dfs(1)
        return ans