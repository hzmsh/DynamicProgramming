n = 4

# DP; Time Complexity O(n), Space O(n)
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
        # we will also include when n = 1 and when n = 2, these two base cases in the dp array:
        methods_per_steps = [1,2]
        
        # find patterns 
        # when n = 3, 3 is n = 2 + n = 1, where there are 2 methods for n = 2, and 1 method for n = 1, total = 3
        # when n = 4, 4 is n = 3 + n = 2, where there are 3 methods for n = 3, and 2 methods for n = 2, total = 5
        for i in range(2,n+1):
            methods_per_steps.append(methods_per_steps[i-1]+methods_per_steps[i-2])
        return(methods_per_steps[n-1])
        
out = Solution().climbStairs(n)
out