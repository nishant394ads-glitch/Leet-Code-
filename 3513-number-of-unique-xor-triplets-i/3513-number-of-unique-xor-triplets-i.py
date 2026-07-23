class Solution:
    def uniqueXorTriplets(self, nums):
        n = len(nums)

        if n <= 2:
            return n

        return 1 << n.bit_length()