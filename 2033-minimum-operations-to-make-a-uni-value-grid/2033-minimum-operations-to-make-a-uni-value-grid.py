from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = []
        
        # Flatten grid
        for row in grid:
            arr.extend(row)
        
        # Check if possible
        rem = arr[0] % x
        for num in arr:
            if num % x != rem:
                return -1
        
        # Sort and choose median
        arr.sort()
        median = arr[len(arr) // 2]
        
        # Count operations
        operations = 0
        for num in arr:
            operations += abs(num - median) // x
        
        return operations