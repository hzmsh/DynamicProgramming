class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # create empty dp array
        dp = [[] for _ in range(n + 1)]
        
        # base case
        dp[0] = ['']
        
        # find patterns
        for i in range(1, n + 1):
            for j in range(i):
                for left in dp[j]:
                    for right in dp[i - j - 1]:
                        dp[i].append(f"({left}){right}")

        print("Generated DP Array after filling = ", dp)
        return dp[n]

# Example usage
sol = Solution()
n = 3
print("Output:", sol.generateParenthesis(n))
