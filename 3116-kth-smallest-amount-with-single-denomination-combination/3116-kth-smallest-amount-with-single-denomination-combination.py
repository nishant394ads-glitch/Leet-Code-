from math import gcd
from itertools import combinations

class Solution:
    def findKthSmallest(self, coins, k):
        n = len(coins)

        # Remove redundant coins.
        # If a coin is a multiple of a smaller coin,
        # all its multiples are already covered.
        coins.sort()
        useful = []

        for coin in coins:
            if not any(coin % x == 0 for x in useful):
                useful.append(coin)

        coins = useful
        n = len(coins)

        def lcm(a, b):
            return a // gcd(a, b) * b

        # Store LCM for every subset
        subsets = []

        for mask in range(1, 1 << n):
            value = 1
            bits = 0
            valid = True

            for i in range(n):
                if mask & (1 << i):
                    value = lcm(value, coins[i])
                    bits += 1

                    # If LCM is already too large, it won't
                    # contribute for practical x values.
                    if value > 10**18:
                        valid = False
                        break

            if valid:
                subsets.append((value, bits))

        def count(x):
            total = 0

            for value, bits in subsets:
                if value > x:
                    continue

                amount = x // value

                if bits % 2 == 1:
                    total += amount
                else:
                    total -= amount

            return total

        # k-th value is at most k * min(coins)
        left = 1
        right = k * coins[0]

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left