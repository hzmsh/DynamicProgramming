class Solution:
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        memo = {}

        def countOnes(x):
            if x == 0:
                return 0
            if x in memo:
                return memo[x]
            
            result = countOnes(x >> 1) + (x & 1)
            memo[x] = result
            return result

        result = [countOnes(i) for i in range(n + 1)]
        print("Calculated bits count recursively = ", result)
        return result

# Example usage
sol = Solution()
n = 5
print("Output:", sol.countBits(n))
