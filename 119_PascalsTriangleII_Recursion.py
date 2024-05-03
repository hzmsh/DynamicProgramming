class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        memo = {}

        def generate(row, col):
            if col == 0 or col == row:
                return 1
            if (row, col) in memo:
                return memo[(row, col)]
            
            # find patterns
            memo[(row, col)] = generate(row - 1, col - 1) + generate(row - 1, col)
            return memo[(row, col)]

        return [generate(rowIndex, i) for i in range(rowIndex + 1)]

# Example usage
sol = Solution()
rowIndex = 3
print("Output:", sol.getRow(rowIndex))
