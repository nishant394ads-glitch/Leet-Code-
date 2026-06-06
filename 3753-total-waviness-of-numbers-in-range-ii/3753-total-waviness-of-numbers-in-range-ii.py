from functools import lru_cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def solve(n: int) -> int:
            if n < 0:
                return 0

            digits = list(map(int, str(n)))

            @lru_cache(None)
            def dp(pos, tight, k, prev2, prev1):
                if pos == len(digits):
                    return (1, 0)  # (count of numbers, total waviness)

                limit = digits[pos] if tight else 9

                total_count = 0
                total_wavy = 0

                for d in range(limit + 1):
                    ntight = tight and (d == limit)

                    if k == 0:
                        if d == 0:
                            cnt, wav = dp(pos + 1, ntight, 0, 0, 0)
                            total_count += cnt
                            total_wavy += wav
                        else:
                            cnt, wav = dp(pos + 1, ntight, 1, 0, d)
                            total_count += cnt
                            total_wavy += wav

                    elif k == 1:
                        cnt, wav = dp(pos + 1, ntight, 2, prev1, d)
                        total_count += cnt
                        total_wavy += wav

                    else:  # k == 2 (at least two digits already formed)
                        add = 1 if (
                            (prev1 > prev2 and prev1 > d) or
                            (prev1 < prev2 and prev1 < d)
                        ) else 0

                        cnt, wav = dp(pos + 1, ntight, 2, prev1, d)

                        total_count += cnt
                        total_wavy += wav + cnt * add

                return (total_count, total_wavy)

            return dp(0, True, 0, 0, 0)[1]

        return solve(num2) - solve(num1 - 1)