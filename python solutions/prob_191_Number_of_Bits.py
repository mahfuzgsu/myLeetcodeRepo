class Solution:
    def hammingWeight(self, n: int) -> int:
        
        count = 0
        
        idx = 0
        
        while n:
            if n % 2:
                count += 1
            n //=2
            
        
        return count