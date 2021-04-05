import numpy as np


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = np.zeros((m, n)).astype('int')
    
        dp[m-1, :] = 1
        dp[:, n-1] = 1

        for j in range(m-2, -1, -1):
            for i in range(n-2, -1, -1):
                dp[j, i] = dp[j+1, i] + dp[j, i+1]

        return dp[0, 0]

        
        
        
        