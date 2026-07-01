from collections import deque
from typing import List

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # Step 1: Distance from nearest thief using Multi-source BFS
        dist = [[-1] * n for _ in range(n)]
        q = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

        # Check if a path exists with safeness >= val
        def canReach(val):
            if dist[0][0] < val:
                return False

            visited = [[False] * n for _ in range(n)]
            q = deque([(0, 0)])
            visited[0][0] = True

            while q:
                x, y = q.popleft()
                if x == n - 1 and y == n - 1:
                    return True

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if (
                        0 <= nx < n
                        and 0 <= ny < n
                        and not visited[nx][ny]
                        and dist[nx][ny] >= val
                    ):
                        visited[nx][ny] = True
                        q.append((nx, ny))

            return False

        low, high = 0, max(max(row) for row in dist)
        ans = 0

        while low <= high:
            mid = (low + high) // 2
            if canReach(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans