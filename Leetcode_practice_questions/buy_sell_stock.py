#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-interview-150

#Solution
def maxProfit(prices):
        buy_prices=prices[0]
        profit=0
        for p in prices[1:]:
            if buy_prices>p:
                buy_prices=p
            profit=max(profit,p-buy_prices)
        return profit
