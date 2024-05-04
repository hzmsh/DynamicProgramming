n = 4

# Recursion; Time Complexity O(2^n), Space O(n)
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # base case
        if n == 0:
            return(0)
        if n == 1:
            return(1)
        if n == 2:
            return(2)
        
        # create dp array
        # we will also include two base cases in the dp array:
        
        # find patterns
        # when n = 2, we can do 1 + 1, or 2 
        # when n = 3, 3 is n = 2 + n = 1, where there are 2 methods for n = 2, and 1 method for n = 1, total = 3
        # when n = 4, 4 is n = 3 + n = 2, where there are 3 methods for n = 3, and 2 methods for n = 2, total = 5

        return(self.climbStairs(n-1) + self.climbStairs(n-2))
        
out = Solution().climbStairs(n)
out