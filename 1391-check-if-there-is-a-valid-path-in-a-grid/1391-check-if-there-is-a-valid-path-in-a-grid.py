from collections import deque

class Solution:
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])

        # Directions: (dx, dy)
        up = (-1, 0)
        down = (1, 0)
        left = (0, -1)
        right = (0, 1)

        # Allowed moves for each street type
        moves = {
            1: [left, right],
            2: [up, down],
            3: [left, down],
            4: [right, down],
            5: [left, up],
            6: [right, up]
        }

        visited = [[False] * n for _ in range(m)]
        q = deque([(0, 0)])
        visited[0][0] = True

        while q:
            x, y = q.popleft()

            if x == m - 1 and y == n - 1:
                return True

            for dx, dy in moves[grid[x][y]]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    # Check if neighbor connects back
                    if (-dx, -dy) in moves[grid[nx][ny]]:
                        visited[nx][ny] = True
                        q.append((nx, ny))

        return False