class Solution:
    def singleNumber(self, arr):
        xorr = 0

        for num in arr:
            xorr ^= num

        return xorr

