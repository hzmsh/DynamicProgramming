class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # create empty dp array
        triangle = []

        # base case
        for row_number in range(numRows):
            # Each row has one more element than its row number
            row = [None for _ in range(row_number + 1)]
            row[0], row[-1] = 1, 1  # First and last element are always 1

            # find patterns
            for j in range(1, len(row) - 1):
                row[j] = triangle[row_number - 1][j - 1] + triangle[row_number - 1][j]

            triangle.append(row)

        print("Generated Pascal's Triangle = ", triangle)
        return triangle

# Example usage
sol = Solution()
numRows = 5
print("Output:", sol.generate(numRows))
