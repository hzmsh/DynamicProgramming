class Solution:
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # create empty dp array
        dp = [False] * (n + 1)

        # base case
        dp[1] = False  # If n = 1, Alice can't make a move and loses immediately

        # find patterns
        for i in range(2, n + 1):
            for x in range(1, i):
                if i % x == 0 and not dp[i - x]:
                    dp[i] = True
                    break

        print("Generated DP Array after filling = ", dp)
        return dp[n]

# Example usage
sol = Solution()
n = 2
print("Output:", sol.divisorGame(n))
