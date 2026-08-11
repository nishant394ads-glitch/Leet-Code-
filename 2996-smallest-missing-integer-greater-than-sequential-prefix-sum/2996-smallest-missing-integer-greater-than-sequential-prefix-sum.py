class Solution:
    def missingInteger(self, nums):
    
        total = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
            else:
                break

        seen = set(nums)

        while total in seen:
            total += 1

        return total