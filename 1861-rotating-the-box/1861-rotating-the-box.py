class Solution:
    def rotateTheBox(self, boxGrid):
        m, n = len(boxGrid), len(boxGrid[0])

        # Step 1: Apply gravity (move stones to the right)
        for i in range(m):
            empty = n - 1  # position to place next stone
            for j in range(n - 1, -1, -1):
                if boxGrid[i][j] == '*':
                    empty = j - 1  # reset after obstacle
                elif boxGrid[i][j] == '#':
                    # move stone to 'empty' position
                    boxGrid[i][j], boxGrid[i][empty] = '.', '#'
                    empty -= 1

        # Step 2: Rotate matrix 90° clockwise
        result = [[None] * m for _ in range(n)]
        
        for i in range(m):
            for j in range(n):
                result[j][m - 1 - i] = boxGrid[i][j]

        return result