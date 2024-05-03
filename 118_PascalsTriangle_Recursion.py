class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 1:
            return [[1]]

        # base case
        elif numRows == 2:
            return [[1], [1, 1]]

        # find patterns
        else:
            result = self.generate(numRows - 1)
            last_row = result[-1]
            current_row = [1]
            for i in range(1, numRows - 1):
                current_row.append(last_row[i - 1] + last_row[i])
            current_row.append(1)
            result.append(current_row)
            return result

# Example usage
sol = Solution()
numRows = 5
print("Output:", sol.generate(numRows))
