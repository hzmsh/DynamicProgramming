class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        
        # create empty dp array
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # base case
        for i in range(m + 1):
            dp[i][0] = i  # deletion to form empty word2
        for j in range(n + 1):
            dp[0][j] = j  # insertion to form word2 from empty word1
        
        # find patterns
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  # characters match, no operation needed
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j],    # deletion
                                       dp[i][j - 1],    # insertion
                                       dp[i - 1][j - 1])  # substitution

        print("Generated DP Array after filling = ", dp)
        return dp[m][n]

# Example usage
sol = Solution()
word1 = "horse"
word2 = "ros"
print("Output:", sol.minDistance(word1, word2))
