class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def checkSubsequence(i, j):
            # base case
            if i == len(s):
                return True
            if j == len(t):
                return False
            
            # find patterns
            if s[i] == t[j]:
                return checkSubsequence(i + 1, j + 1)
            else:
                return checkSubsequence(i, j + 1)
        
        result = checkSubsequence(0, 0)
        print("Calculated recursively = ", result)
        return result

# Example usage
sol = Solution()
s = "abc"
t = "ahbgdc"
print("Output:", sol.isSubsequence(s, t))
