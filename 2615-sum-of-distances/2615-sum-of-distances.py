class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        from collections import defaultdict
        
        n = len(nums)
        ans = [0] * n
        mp = defaultdict(list)
        
        # Store indices for each number
        for i, num in enumerate(nums):
            mp[num].append(i)
        
        # Process each group
        for positions in mp.values():
            m = len(positions)
            if m == 1:
                continue
            
            # Prefix sums of indices
            prefix = [0] * (m + 1)
            for i in range(m):
                prefix[i + 1] = prefix[i] + positions[i]
            
            for i in range(m):
                left = positions[i] * i - prefix[i]
                right = (prefix[m] - prefix[i + 1]) - positions[i] * (m - i - 1)
                ans[positions[i]] = left + right
        
        return ans