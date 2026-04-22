class Solution:
    def twoEditWords(self, queries, dictionary):
        ans = []

        for q in queries:
            for d in dictionary:
                diff = sum(1 for a, b in zip(q, d) if a != b)
                if diff <= 2:
                    ans.append(q)
                    break

        return ans