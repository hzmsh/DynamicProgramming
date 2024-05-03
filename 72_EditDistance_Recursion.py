class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        def recurse(i, j):
            # base case
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            
            # find patterns
            if word1[i] == word2[j]:
                return recurse(i + 1, j + 1)
            else:
                insert = 1 + recurse(i, j + 1)
                delete = 1 + recurse(i + 1, j)
                replace = 1 + recurse(i + 1, j + 1)
                return min(insert, delete, replace)
        
        result = recurse(0, 0)
        print("Calculated minimum edit distance recursively = ", result)
        return result

# Example usage
sol = Solution()
word1 = "horse"
word2 = "ros"
print("Output:", sol.minDistance(word1, word2))
