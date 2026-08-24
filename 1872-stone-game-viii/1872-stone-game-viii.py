class Solution:
    def stoneGameVIII(self, stones):
        total = 0

        # Total prefix sum
        for x in stones:
            total += x

        dp = total

        # Remove the last stone from the prefix sum
        for i in range(len(stones) - 2, 0, -1):
            total -= stones[i + 1]
            dp = max(dp, total - dp)

        return dp 