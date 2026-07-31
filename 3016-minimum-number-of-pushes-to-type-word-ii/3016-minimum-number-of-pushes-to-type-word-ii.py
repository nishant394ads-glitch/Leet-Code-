class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = [0] * 26

        # Count frequency of each letter
        for ch in word:
            freq[ord(ch) - ord('a')] += 1

        # Sort frequencies in descending order
        freq.sort(reverse=True)

        ans = 0

        # Calculate minimum pushes
        for i, f in enumerate(freq):
            if f == 0:
                break
            ans += f * (i // 8 + 1)

        return ans