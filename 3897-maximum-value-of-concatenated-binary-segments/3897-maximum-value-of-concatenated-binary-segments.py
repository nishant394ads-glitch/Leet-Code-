from functools import cmp_to_key

class Solution:
    def maxValue(self, nums1, nums0):
        MOD = 10**9 + 7
        segs = list(zip(nums1, nums0))

        def cmp(x, y):
            a1, b1 = x
            a2, b2 = y
            x_pure = (b1 == 0)
            y_pure = (b2 == 0)
            if x_pure and not y_pure:
                return -1
            if y_pure and not x_pure:
                return 1
            if x_pure and y_pure:
                return 0
            # both have trailing zeros
            if a1 != a2:
                return -1 if a1 > a2 else 1
            if b1 != b2:
                return -1 if b1 < b2 else 1
            return 0

        segs.sort(key=cmp_to_key(cmp))

        total_len = sum(a + b for a, b in segs)
        pow2 = [1] * (total_len + 1)
        for i in range(1, total_len + 1):
            pow2[i] = pow2[i - 1] * 2 % MOD

        val = 0
        for a, b in segs:
            seg_val = (pow2[a] - 1) * pow2[b] % MOD
            val = (val * pow2[a + b] + seg_val) % MOD

        return val
        