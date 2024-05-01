class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def findMaxCrossingSum(arr, l, m, h):
            # Include elements on left of mid.
            sm = 0
            left_sum = float('-inf')

            for i in range(m, l-1, -1):
                sm = sm + arr[i]
                if (sm > left_sum):
                    left_sum = sm

            # Include elements on right of mid
            sm = 0
            right_sum = float('-inf')
            for i in range(m + 1, h + 1):
                sm = sm + arr[i]
                if (sm > right_sum):
                    right_sum = sm

            # Return sum of elements on left and right of mid
            return max(left_sum + right_sum, left_sum, right_sum)

        # Returns sum of maxium sum subarray in aa[l..h]
        def maxSubArraySum(arr, l, h):
            # base case: only one element
            if (l == h):
                return arr[l]

            # Find middle point
            m = (l + h) // 2

            # Return maximum of following three possible cases
            # a) Maximum subarray sum in left half
            # b) Maximum subarray sum in right half
            # c) Maximum subarray sum such that the subarray crosses the midpoint 
            return max(maxSubArraySum(arr, l, m),
                   maxSubArraySum(arr, m+1, h),
                   findMaxCrossingSum(arr, l, m, h))

        # Driver method to test the above function
        result = maxSubArraySum(nums, 0, len(nums)-1)
        print("Calculated maximum subarray sum recursively = ", result)
        return result

# Example usage
sol = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print("Output:", sol.maxSubArray(nums))
