class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        memo = {}

        def dfs(i, j, k):
            if (i, j) in memo:
                return memo[(i, j)]
            
            # base case
            if i == len(s1) and j == len(s2) and k == len(s3):
                return True
            if k == len(s3):
                return False
            
            # find patterns
            ans = False
            if i < len(s1) and s1[i] == s3[k]:
                ans |= dfs(i + 1, j, k + 1)
            if j < len(s2) and s2[j] == s3[k]:
                ans |= dfs(i, j + 1, k + 1)
            
            memo[(i, j)] = ans
            return ans
        
        result = dfs(0, 0, 0)
        print("Calculated interleaving recursively = ", result)
        return result

# Example usage
sol = Solution()
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
print("Output:", sol.isInterleave(s1, s2, s3))
