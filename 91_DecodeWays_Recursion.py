class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        memo = {}
        
        def decode(i):
            # base case
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            if i == len(s)-1:
                return 1
            
            # Memoization lookup
            if i in memo:
                return memo[i]
            
            # find patterns
            result = decode(i+1)
            if i < len(s)-1 and (s[i] == '1' or (s[i] == '2' and s[i+1] in '0123456')):
                result += decode(i+2)
            
            memo[i] = result
            return result
        
        result = decode(0)
        print("Calculated number of ways recursively = ", result)
        return result

# Example usage
sol = Solution()
s = "226"
print("Output:", sol.numDecodings(s))
