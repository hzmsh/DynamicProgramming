class Solution:
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # create empty dp array
        dp = [0] * (n + 1)

        # find patterns
        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)

        print("Generated DP Array after filling = ", dp)
        return dp

# Example usage
sol = Solution()
n = 5
print("Output:", sol.countBits(n))
