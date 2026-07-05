class Solution:
    def pathsWithMaxScore(self, board):
        MOD = 10 ** 9 + 7
        n = len(board)

        NEG = -10 ** 9

        dpScore = [[NEG] * n for _ in range(n)]
        dpWays = [[0] * n for _ in range(n)]

        dpScore[n - 1][n - 1] = 0
        dpWays[n - 1][n - 1] = 1

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                if board[i][j] == 'X':
                    continue

                if i == n - 1 and j == n - 1:
                    continue

                best = NEG
                ways = 0

                for x, y in ((i + 1, j), (i, j + 1), (i + 1, j + 1)):
                    if x < n and y < n:
                        if dpScore[x][y] > best:
                            best = dpScore[x][y]
                            ways = dpWays[x][y]
                        elif dpScore[x][y] == best and best != NEG:
                            ways = (ways + dpWays[x][y]) % MOD

                if best == NEG:
                    continue

                if board[i][j] in ('E', 'S'):
                    val = 0
                else:
                    val = int(board[i][j])

                dpScore[i][j] = best + val
                dpWays[i][j] = ways % MOD

        if dpWays[0][0] == 0:
            return [0, 0]

        return [dpScore[0][0], dpWays[0][0]]