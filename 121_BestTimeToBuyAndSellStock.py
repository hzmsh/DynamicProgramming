class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        min_price = float('inf')
        max_profit = 0
        
        # find patterns
        for price in prices:
            if price < min_price:
                min_price = price  # Update minimum price so far
            elif price - min_price > max_profit:
                max_profit = price - min_price  # Calculate profit if sold today

        print("Maximum Profit = ", max_profit)
        return max_profit

# Example usage
sol = Solution()
prices = [7,1,5,3,6,4]
print("Output:", sol.maxProfit(prices))
