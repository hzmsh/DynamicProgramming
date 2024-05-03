class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == '0':
            return 0
        
        n = len(s)
        # create empty dp array
        dp = [0] * (n + 1)

        # base case
        dp[0] = 1  # Empty string has one way to decode
        dp[1] = 1  # The first character has one way to decode if not '0'

        # find patterns
        for i in range(2, n + 1):
            # Single digit decode (must not be '0')
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            
            # Two digit decode (must be between "10" and "26")
            two_digit = int(s[i-2:i])  # Convert the two characters to a number
            if 10 <= two_digit <= 26:
                dp[i] += dp[i-2]

        print("Generated DP Array after filling = ", dp)
        return dp[n]

# Example usage
sol = Solution()
s = "226"
print("Output:", sol.numDecodings(s))
