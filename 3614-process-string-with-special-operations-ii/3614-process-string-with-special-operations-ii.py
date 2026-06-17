class Solution:
    def processStr(self, s: str, k: int) -> str:
        LIMIT = 10**15 + 1

        lengths = []
        length = 0

        for ch in s:
            if 'a' <= ch <= 'z':
                length = min(LIMIT, length + 1)
            elif ch == '*':
                if length > 0:
                    length -= 1
            elif ch == '#':
                length = min(LIMIT, length * 2)
            else:  # '%'
                pass
            lengths.append(length)

        if k >= length:
            return '.'

        L = length

        for i in range(len(s) - 1, -1, -1):
            ch = s[i]

            if 'a' <= ch <= 'z':
                if k == L - 1:
                    return ch
                L -= 1

            elif ch == '*':
                if L > 0:
                    L += 1

            elif ch == '#':
                prev = L // 2
                if prev > 0:
                    k %= prev
                L = prev

            else:  # '%'
                if L > 0:
                    k = L - 1 - k

        return '.'