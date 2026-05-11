class Solution:
    def separateDigits(self, nums):
        answer = []
        
        for num in nums:
            for digit in str(num):
                answer.append(int(digit))
        
        return answer