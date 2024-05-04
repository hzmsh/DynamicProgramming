class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # create empty dp array
        dp = [[False] * (len(s) + 1) for _ in range(len(t) + 1)]

        # base case: an empty s is a subsequence of any t
        for i in range(len(t) + 1):
            dp[i][0] = True

        # find patterns
        for i in range(1, len(t) + 1):
            for j in range(1, len(s) + 1):
                if t[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j]

        print("Generated DP Table after filling = ", dp)
        return dp[len(t)][len(s)]

# Example usage
sol = Solution()
s = "abc"
t = "ahbgdc"
print("Output:", sol.isSubsequence(s, t))
