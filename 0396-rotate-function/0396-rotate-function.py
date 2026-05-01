class Solution:
    def maxRotateFunction(self, nums):
        n = len(nums)
        
        total_sum = sum(nums)
        F = sum(i * num for i, num in enumerate(nums))
        
        max_val = F
        
        for k in range(1, n):
            F = F + total_sum - n * nums[n - k]
            max_val = max(max_val, F)
        
        return max_val