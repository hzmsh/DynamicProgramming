class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Base case: A single character or empty string is a palindrome
        if len(s) < 2 or s == s[::-1]:
            return s
        
        def isPalindrome(l, r):
            # Check if the substring s[l:r+1] is a palindrome
            return s[l:r+1] == s[l:r+1][::-1]
        
        # Recursive function to find longest palindrome
        def findLongestPalindrome(l, r):
            if l >= r:
                return s[l:r+1]

            if isPalindrome(l, r):
                return s[l:r+1]

            # Try removing the right end or the left end character and recurse
            left = findLongestPalindrome(l, r-1)
            right = findLongestPalindrome(l+1, r)
            
            # Return the longer palindrome found
            if len(left) > len(right):
                return left
            else:
                return right
        
        return findLongestPalindrome(0, len(s) - 1)

# Example usage:
sol = Solution()
s = "babad"
print("Output:", sol.longestPalindrome(s))
