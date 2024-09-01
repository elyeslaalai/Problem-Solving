class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) == 1:
            return 0
        
        lowest_price, highest_price = prices[0], prices[0]
        profit = 0

        for i in range(1, len(prices)):
            new_price = prices[i]
            if new_price < lowest_price:
                lowest_price = new_price
            if new_price > lowest_price:
                profit = max(profit, new_price - lowest_price)
                highest_price = new_price
        
        return profit

        # [7, 1, 5, 3, 6, 4]
        # min = 7, max = 7
        # min = 1, max = 1
        # min = 1, max = 5
