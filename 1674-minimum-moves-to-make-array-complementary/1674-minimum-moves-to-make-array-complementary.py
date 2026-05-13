class Solution:
    def minMoves(self, nums, limit):
        n = len(nums)

        diff = [0] * (2 * limit + 2)

        for i in range(n // 2):
            a = nums[i]
            b = nums[n - 1 - i]

            low = min(a, b) + 1
            high = max(a, b) + limit
            s = a + b

            # Initially assume 2 moves
            diff[2] += 2

            # 1 move range
            diff[low] -= 1

            # 0 move at exact sum
            diff[s] -= 1
            diff[s + 1] += 1

            # Back to 2 moves after high
            diff[high + 1] += 1

        ans = float('inf')
        curr = 0

        for target in range(2, 2 * limit + 1):
            curr += diff[target]
            ans = min(ans, curr)

        return ans