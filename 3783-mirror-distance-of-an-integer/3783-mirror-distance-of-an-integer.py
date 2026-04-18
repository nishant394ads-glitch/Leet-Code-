class Solution:
    def mirrorDistance(self, n: int) -> int:
        rev = int(str(n)[::-1])   # reverse digits
        return abs(n - rev)