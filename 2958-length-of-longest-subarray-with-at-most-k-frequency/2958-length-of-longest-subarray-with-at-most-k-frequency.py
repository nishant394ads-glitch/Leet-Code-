from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums, k):
        freq = defaultdict(int)
        left = 0
        ans = 0

        for right in range(len(nums)):
            freq[nums[right]] += 1

            # Window is invalid
            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                left += 1

            # Current window is good
            ans = max(ans, right - left + 1)

        return ans