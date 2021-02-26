def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
    n = len(prices)
    cost = 0
    maxcost = 0
    min_price = prices[0]
    
    if(n==0):
        return 0
    
    for i in range(n):
        min_price = min(min_price,prices[i])
        cost = prices[i] - min_price
        maxcost = max(maxcost, cost)
        
    return maxcost
    