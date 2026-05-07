from typing import List

class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # suffix minimum
        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])

        ans = [0] * n

        start = 0
        current_max = nums[0]

        for i in range(n - 1):
            current_max = max(current_max, nums[i])

            # split component
            if current_max <= suffix_min[i + 1]:
                block_max = max(nums[start:i + 1])

                for j in range(start, i + 1):
                    ans[j] = block_max

                start = i + 1
                current_max = nums[start]

        # last component
        block_max = max(nums[start:])

        for j in range(start, n):
            ans[j] = block_max

        return ans