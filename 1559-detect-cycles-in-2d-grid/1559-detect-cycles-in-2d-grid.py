class Solution:
    def containsCycle(self, grid):
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(x, y, px, py, char):
            if visited[x][y]:
                return True

            visited[x][y] = True

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == char:
                    # Skip parent cell
                    if nx == px and ny == py:
                        continue

                    if dfs(nx, ny, x, y, char):
                        return True

            return False

        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    if dfs(i, j, -1, -1, grid[i][j]):
                        return True

        return False