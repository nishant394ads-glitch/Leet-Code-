class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {}
        current_rank = 1

        for num in sorted(arr):
            if num not in rank:
                rank[num] = current_rank
                current_rank += 1

        return [rank[num] for num in arr]