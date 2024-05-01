class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n < 1:
            return ""
        
        # Base case
        dp = [[False] * n for _ in range(n)]
        start = 0
        max_length = 1
        
        # Every single character is a palindrome of length 1
        for i in range(n):
            dp[i][i] = True
        
        # Check for two-character palindromes
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                start = i
                max_length = 2
        
        print("Pre-generated DP Array = ", dp)
        
        # Fill DP array for substrings longer than 2 characters
        for length in range(3, n + 1):  # length ranges from 3 to n
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    start = i
                    max_length = length
        
        print("Generated DP Array after filling = ", dp)
        
        # Return the longest palindrome substring
        return s[start:start + max_length]

# Example usage:
sol = Solution()
s = "babad"
print("Output:", sol.longestPalindrome(s))
