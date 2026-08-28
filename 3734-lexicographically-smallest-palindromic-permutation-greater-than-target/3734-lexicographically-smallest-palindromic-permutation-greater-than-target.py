class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Count characters
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1

        # Check palindrome possibility
        odd = 0
        middle = ""

        for i in range(26):
            if cnt[i] % 2:
                odd += 1
                middle = chr(i + 97)

        if odd > 1:
            return ""

        # Frequency of characters in the left half
        half_cnt = [x // 2 for x in cnt]
        m = n // 2

        def make_palindrome(left):
            left = ''.join(left)
            return left + middle + left[::-1]

        # ------------------------------------------------
        # Find the smallest half >= target[:m]
        # ------------------------------------------------

        t = target[:m]

        # Check if target's first half itself is possible
        remaining = half_cnt[:]
        possible = True

        for ch in t:
            c = ord(ch) - 97

            if remaining[c] == 0:
                possible = False
                break

            remaining[c] -= 1

        # If target half is possible, test its palindrome
        if possible:
            candidate = make_palindrome(t)

            # Important:
            # The palindrome can be > target even when
            # its first half is exactly equal to target[:m].
            if candidate > target:
                return candidate

        # ------------------------------------------------
        # Find the smallest half strictly greater than t
        # ------------------------------------------------

        for i in range(m - 1, -1, -1):

            remaining = half_cnt[:]

            # Match target prefix [0 ... i-1]
            possible = True

            for j in range(i):
                c = ord(t[j]) - 97

                if remaining[c] == 0:
                    possible = False
                    break

                remaining[c] -= 1

            if not possible:
                continue

            # At position i, choose the smallest
            # character greater than target[i]
            tc = ord(t[i]) - 97

            for c in range(tc + 1, 26):

                if remaining[c] == 0:
                    continue

                remaining[c] -= 1

                left = list(t[:i])
                left.append(chr(c + 97))

                # Fill remaining positions as small as possible
                for x in range(26):
                    left.extend(
                        [chr(x + 97)] * remaining[x]
                    )

                return make_palindrome(left)

        return ""