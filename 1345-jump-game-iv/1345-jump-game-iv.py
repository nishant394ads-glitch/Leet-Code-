from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr):
        n = len(arr)

        if n == 1:
            return 0

        mp = defaultdict(list)

        for i, v in enumerate(arr):
            mp[v].append(i)

        q = deque([(0, 0)])
        vis = {0}

        while q:
            i, steps = q.popleft()

            if i == n - 1:
                return steps

            nxt = []

            if i + 1 < n:
                nxt.append(i + 1)

            if i - 1 >= 0:
                nxt.append(i - 1)

            nxt.extend(mp[arr[i]])

            for j in nxt:
                if j not in vis:
                    vis.add(j)
                    q.append((j, steps + 1))

            # prevent repeated processing
            mp[arr[i]].clear()