class Solution:
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        memo = {}
        
        def canWin(current):
            if current in memo:
                return memo[current]
            if current == 1:
                return False

            # find patterns
            for x in range(1, current):
                if current % x == 0 and not canWin(current - x):
                    memo[current] = True
                    return True
            
            memo[current] = False
            return False

        result = canWin(n)
        print("Calculated recursively = ", result)
        return result

# Example usage
sol = Solution()
n = 2
print("Output:", sol.divisorGame(n))
