from datetime import datetime
import matplotlib.pyplot as plt

# Section 1
start = datetime.now()
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

end = datetime.now()
print(end - start)


# Section 2
start = datetime.now()
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
end = datetime.now()
print(end - start)


# Plot the Time Consumption for Recursion
time_list = [2,3,5,8,15,21,40,59,91]
n_list = [34,35,36,37,38,39,40,41,42]

plt.plot(n_list,time_list)