class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        def calculateMaxProfit(index, canBuy):
            # base case
            if index >= len(prices):
                return 0
            
            if canBuy:
                # find patterns
                # Buy today or do not buy
                return max(calculateMaxProfit(index + 1, False) - prices[index],
                           calculateMaxProfit(index + 1, True))
            else:
                # Sell today or do not sell
                return max(calculateMaxProfit(index + 1, True) + prices[index],
                           calculateMaxProfit(index + 1, False))
        
        result = calculateMaxProfit(0, True)
        print("Calculated maximum profit recursively = ", result)
        return result

# Example usage
sol = Solution()
prices = [7,1,5,3,6,4]
print("Output:", sol.maxProfit(prices))
