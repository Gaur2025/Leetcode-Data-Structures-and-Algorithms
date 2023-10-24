class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buyIndex, sellIndex = 0, 1

        profit = 0

        while sellIndex < len(prices):
            # check if any profit is made
            tempProfit = prices[sellIndex] - prices[buyIndex]
            if tempProfit > 0: 
                profit = max(profit, tempProfit)
            else:
                # we move to other buy time
                buyIndex = sellIndex

            sellIndex += 1

        return profit

        