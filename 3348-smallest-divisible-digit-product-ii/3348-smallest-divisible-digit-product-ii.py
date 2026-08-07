class Solution:

    def smallestNumber(self, num: str, t: int) -> str:

        # Factor t into 2, 3, 5, 7
        a = b = c = d = 0

        while t % 2 == 0:
            a += 1
            t //= 2

        while t % 3 == 0:
            b += 1
            t //= 3

        while t % 5 == 0:
            c += 1
            t //= 5

        while t % 7 == 0:
            d += 1
            t //= 7

        # Cannot be formed using digits 1..9
        if t != 1:
            return "-1"

        # Prime factor contribution of each digit
        p2 = [0, 0, 1, 0, 2, 0, 1, 0, 3, 0]
        p3 = [0, 0, 0, 1, 0, 0, 1, 0, 0, 2]
        p5 = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
        p7 = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]

        from functools import lru_cache

        INF = 10**9

        @lru_cache(None)
        def solve(a, b, c, d):

            if a == 0 and b == 0 and c == 0 and d == 0:
                return 0

            ans = INF

            # 1 is deliberately excluded.
            # It does not reduce the state.
            for x in range(2, 10):

                na = max(0, a - p2[x])
                nb = max(0, b - p3[x])
                nc = max(0, c - p5[x])
                nd = max(0, d - p7[x])

                if (na, nb, nc, nd) == (a, b, c, d):
                    continue

                ans = min(
                    ans,
                    1 + solve(na, nb, nc, nd)
                )

            return ans

        def build(length, a, b, c, d):

            ans = []

            for pos in range(length):

                remaining = length - pos - 1

                for x in range(1, 10):

                    na = max(0, a - p2[x])
                    nb = max(0, b - p3[x])
                    nc = max(0, c - p5[x])
                    nd = max(0, d - p7[x])

                    if solve(na, nb, nc, nd) <= remaining:

                        ans.append(str(x))

                        a, b, c, d = na, nb, nc, nd
                        break

            return ''.join(ans)

        # Minimum digits required
        required = solve(a, b, c, d)

        # If impossible even theoretically
        if required >= INF:
            return "-1"

        # Need a longer number
        if required > len(num):
            return build(required, a, b, c, d)

        n = len(num)

        # Remaining factor requirements after each prefix
        r2 = [0] * (n + 1)
        r3 = [0] * (n + 1)
        r5 = [0] * (n + 1)
        r7 = [0] * (n + 1)

        r2[0] = a
        r3[0] = b
        r5[0] = c
        r7[0] = d

        for i in range(n):

            x = ord(num[i]) - ord('0')

            r2[i + 1] = max(0, r2[i] - p2[x])
            r3[i + 1] = max(0, r3[i] - p3[x])
            r5[i + 1] = max(0, r5[i] - p5[x])
            r7[i + 1] = max(0, r7[i] - p7[x])

        # num itself works
        if (
            '0' not in num
            and r2[n] == 0
            and r3[n] == 0
            and r5[n] == 0
            and r7[n] == 0
        ):
            return num

        # Find first zero.
        # We cannot modify a position AFTER this zero,
        # because the unchanged prefix would contain zero.
        first_zero = num.find('0')

        if first_zero == -1:
            first_zero = n

        # Try changing the rightmost possible position
        for i in range(n - 1, -1, -1):

            # Prefix num[:i] must be zero-free
            if i > first_zero:
                continue

            original = ord(num[i]) - ord('0')

            for x in range(original + 1, 10):

                # x itself must be non-zero
                if x == 0:
                    continue

                na = max(0, r2[i] - p2[x])
                nb = max(0, r3[i] - p3[x])
                nc = max(0, r5[i] - p5[x])
                nd = max(0, r7[i] - p7[x])

                remaining = n - i - 1

                if solve(na, nb, nc, nd) <= remaining:

                    prefix = num[:i]

                    suffix = build(
                        remaining,
                        na,
                        nb,
                        nc,
                        nd
                    )

                    return prefix + str(x) + suffix

        # No same-length solution.
        # Any zero-free number with n+1 digits is larger.
        return build(n + 1, a, b, c, d)