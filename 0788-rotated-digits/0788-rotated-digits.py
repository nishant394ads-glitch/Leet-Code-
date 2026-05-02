class Solution:
    def rotatedDigits(self, n: int) -> int:
        count = 0
        
        for i in range(1, n + 1):
            num = i
            valid = True
            changed = False
            
            while num > 0:
                digit = num % 10
                
                if digit in [3, 4, 7]:
                    valid = False
                    break
                if digit in [2, 5, 6, 9]:
                    changed = True
                
                num //= 10
            
            if valid and changed:
                count += 1
        
        return count