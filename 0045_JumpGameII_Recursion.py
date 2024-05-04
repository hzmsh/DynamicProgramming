class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def minJumps(index):
            # base case
            if index >= len(nums) - 1:
                return 0
            
            # find patterns
            min_steps = float('inf')
            max_jump = min(index + nums[index], len(nums) - 1)
            for next_index in range(index + 1, max_jump + 1):
                steps = 1 + minJumps(next_index)
                min_steps = min(min_steps, steps)
            
            return min_steps
        
        result = minJumps(0)
        print("Calculated minimum jumps recursively = ", result)
        return result

# Example usage
sol = Solution()
nums = [2,3,1,1,4]
print("Output:", sol.jump(nums))
