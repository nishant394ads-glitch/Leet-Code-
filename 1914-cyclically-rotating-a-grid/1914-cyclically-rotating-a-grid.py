class Solution:
    def rotateGrid(self, grid, k):
        m, n = len(grid), len(grid[0])

        layers = min(m, n) // 2

        for layer in range(layers):
            elems = []

            top, left = layer, layer
            bottom, right = m - layer - 1, n - layer - 1

            # top row
            for j in range(left, right + 1):
                elems.append(grid[top][j])

            # right column
            for i in range(top + 1, bottom):
                elems.append(grid[i][right])

            # bottom row
            for j in range(right, left - 1, -1):
                elems.append(grid[bottom][j])

            # left column
            for i in range(bottom - 1, top, -1):
                elems.append(grid[i][left])

            length = len(elems)
            rot = k % length

            # counter-clockwise rotation
            rotated = elems[rot:] + elems[:rot]

            idx = 0

            # fill top row
            for j in range(left, right + 1):
                grid[top][j] = rotated[idx]
                idx += 1

            # fill right column
            for i in range(top + 1, bottom):
                grid[i][right] = rotated[idx]
                idx += 1

            # fill bottom row
            for j in range(right, left - 1, -1):
                grid[bottom][j] = rotated[idx]
                idx += 1

            # fill left column
            for i in range(bottom - 1, top, -1):
                grid[i][left] = rotated[idx]
                idx += 1

        return grid