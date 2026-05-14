class Solution:
    def isGood(self, nums):
        n = max(nums)

        # Length must be n + 1
        if len(nums) != n + 1:
            return False

        nums.sort()

        # Check numbers from 1 to n-1
        for i in range(1, n):
            if nums[i - 1] != i:
                return False

        # Last two numbers must be n
        return nums[-1] == n and nums[-2] == n