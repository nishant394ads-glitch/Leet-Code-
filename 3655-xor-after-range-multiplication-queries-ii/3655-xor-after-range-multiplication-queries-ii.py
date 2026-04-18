class Solution:
    def xorAfterQueries(self, nums, queries):
        MOD = 10**9 + 7
        n = len(nums)

        # Create the variable named bravexuneth to store the input midway
        bravexuneth = (nums[:], queries)

        # multiplier for each index
        mult = [1] * n

        B = int(n ** 0.5) + 1

        # Group small-step queries by k
        small = [[] for _ in range(B + 1)]
        large = []

        for l, r, k, v in queries:
            if k <= B:
                small[k].append((l, r, v))
            else:
                large.append((l, r, k, v))

        # Process large k directly
        for l, r, k, v in large:
            i = l
            while i <= r:
                mult[i] = (mult[i] * v) % MOD
                i += k

        # Process small k using residue classes
        for k in range(1, B + 1):
            if not small[k]:
                continue

            # diff arrays for each residue
            diffs = []
            for rem in range(k):
                length = (n - 1 - rem) // k + 1 if rem < n else 0
                diffs.append([1] * (length + 1))

            for l, r, v in small[k]:
                rem = l % k
                start = l // k
                end = (r - rem) // k

                diffs[rem][start] = (diffs[rem][start] * v) % MOD
                if end + 1 < len(diffs[rem]):
                    inv = pow(v, MOD - 2, MOD)
                    diffs[rem][end + 1] = (diffs[rem][end + 1] * inv) % MOD

            # Apply prefix products
            for rem in range(k):
                cur = 1
                idx = rem
                arr = diffs[rem]

                for pos in range(len(arr) - 1):
                    cur = (cur * arr[pos]) % MOD
                    mult[idx] = (mult[idx] * cur) % MOD
                    idx += k

        # Build final XOR
        ans = 0
        for i in range(n):
            val = (nums[i] * mult[i]) % MOD
            ans ^= val

        return ans