class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)

        # (value, original index)
        arr = sorted((value, i) for i, value in enumerate(nums))

        ans = [0] * n
        start = 0

        while start < n:
            end = start

            # Find the connected group
            while end + 1 < n and arr[end + 1][0] - arr[end][0] <= limit:
                end += 1

            # Get original indices
            indices = sorted(arr[i][1] for i in range(start, end + 1))

            # Values are already sorted
            for i, index in enumerate(indices):
                ans[index] = arr[start + i][0]

            start = end + 1

        return ans