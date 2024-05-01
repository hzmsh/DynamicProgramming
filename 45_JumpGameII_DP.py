class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return 0
        
        # create dp-like variables for tracking progress
        jumps = 0
        current_end = 0
        farthest = 0
        
        # base case
        for i in range(n-1):  # we don't need to jump from the last element
            # find patterns
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest
                if current_end >= n - 1:
                    break

        print("Final number of jumps = ", jumps)
        return jumps

# Example usage
sol = Solution()
nums = [2,3,1,1,4]
print("Output:", sol.jump(nums))
