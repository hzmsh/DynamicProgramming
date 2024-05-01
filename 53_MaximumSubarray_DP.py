class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # base case
        max_current = max_global = nums[0]
        
        # find patterns
        for i in range(1, len(nums)):
            max_current = max(nums[i], max_current + nums[i])
            if max_current > max_global:
                max_global = max_current

        print("Maximum Subarray Sum = ", max_global)
        return max_global

# Example usage
sol = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print("Output:", sol.maxSubArray(nums))
