n = 4

# DP time complexity O(n),Space O(n)
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        # base case
        if n == 0:
            return(0)
        if n == 1:
            return(1)
        # create empty dp array
        dp = [0] * (n + 1)

        # find patterns
        dp[0] = 0
        dp[1] = 1
        
        print("Pre-generated DP Array = ", dp)
        # dp[2] = dp[1] + dp[0]
        # dp[i] = dp[i-1] + dp[i-2]
        
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        print("Generated DP Array after filling = ", dp)
        
        return(dp[n])
        
        
out = Solution().fib(n)
out