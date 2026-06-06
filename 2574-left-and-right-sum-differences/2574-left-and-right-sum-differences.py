from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        left_sum = 0
        answer = []

        for num in nums:
            total -= num  # rightSum
            answer.append(abs(left_sum - total))
            left_sum += num

        return answer