class Solution(object):
    def maxProfit(self, prices):
        maxProfit = 0
        for i in range(len(prices)):
            indexMinNum = prices.index(min(princes))
            indexMaxNum = prices.index(max(princes[indexMinNum::]))
            profit = prices[indexMaxNum] - prices[indexMinNum]
            if profit > maxProfit:
                maxProfit = profit
            prices.pop(indexMinNum)
        return maxProfit
