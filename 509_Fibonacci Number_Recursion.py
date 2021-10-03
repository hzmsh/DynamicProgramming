# Recursion O(2^n), Space O(N)
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
        
        # pattern:
        # ith = i-1th + i-2th
        return(self.fib(n-1) + self.fib(n-2))
        
        
out = Solution().fib(n)
out