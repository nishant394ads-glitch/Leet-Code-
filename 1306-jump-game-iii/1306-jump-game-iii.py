from collections import deque

class Solution:
    def canReach(self, arr, start):
        n = len(arr)

        q = deque([start])
        vis = set([start])

        while q:
            i = q.popleft()

            if arr[i] == 0:
                return True

            for nxt in (i + arr[i], i - arr[i]):
                if 0 <= nxt < n and nxt not in vis:
                    vis.add(nxt)
                    q.append(nxt)

        return False