class Solution:
    def findGCD(self, nums):
        a = min(nums)
        b = max(nums)

        while b:
            a, b = b, a % b

        return a