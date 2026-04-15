class Solution:
    def closestTarget(self, words, target, startIndex):
        n = len(words)
        min_dist = float('inf')
        
        for i in range(n):
            if words[i] == target:
                diff = abs(i - startIndex)
                dist = min(diff, n - diff)
                min_dist = min(min_dist, dist)
        
        return -1 if min_dist == float('inf') else min_dist