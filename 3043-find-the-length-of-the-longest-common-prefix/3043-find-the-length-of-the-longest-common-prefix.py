class Solution:
    def longestCommonPrefix(self, arr1, arr2):
        prefixes = set()

        # Store all prefixes of numbers in arr1
        for num in arr1:
            s = str(num)
            for i in range(1, len(s) + 1):
                prefixes.add(s[:i])

        ans = 0

        # Check prefixes in arr2
        for num in arr2:
            s = str(num)
            for i in range(1, len(s) + 1):
                if s[:i] in prefixes:
                    ans = max(ans, i)

        return ans