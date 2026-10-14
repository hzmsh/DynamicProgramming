class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def backtrack(S, left, right):
            # base case
            if len(S) == 2 * n:
                result.append(S)
                return
            
            # find patterns
            if left < n:
                backtrack(S + '(', left + 1, right)
            if right < left:
                backtrack(S + ')', left, right + 1)

        result = []
        backtrack('', 0, 0)
        return result

# Example usage
sol = Solution()
n = 3
print("Output:", sol.generateParenthesis(n))
