class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        pos = [i for i, c in enumerate(s) if c == '1']

        if len(pos) < k:
            return ""

        ans = None
        best = float('inf')

        for i in range(len(pos) - k + 1):
            l = pos[i]
            r = pos[i + k - 1]

            sub = s[l:r + 1]
            length = len(sub)

            if length < best or (length == best and (ans is None or sub < ans)):
                best = length
                ans = sub

        return ans