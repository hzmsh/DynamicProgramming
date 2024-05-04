from datetime import datetime
import matplotlib.pyplot as plt

time_list = []
n_list = list(range(33,45))

# Main
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

    
for n in n_list:
    start = datetime.now().timestamp()

    out = Solution().climbStairs(n)

    end = datetime.now().timestamp()
    
    difference = end - start
    print("When n = ",n,"Difference = ",difference)
    time_list.append(difference)


# Plot the Time Consumption for Recursion
plt.plot(n_list,time_list)
