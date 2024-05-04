class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # create empty dp array
        row = [1] * (rowIndex + 1)
        
        # find patterns
        for i in range(1, rowIndex):
            # Update the row from the end to start to avoid overwriting elements that are yet to be used
            for j in range(i, 0, -1):
                row[j] += row[j - 1]

        print("Generated Pascal's Triangle Row = ", row)
        return row

# Example usage
sol = Solution()
rowIndex = 3
print("Output:", sol.getRow(rowIndex))
