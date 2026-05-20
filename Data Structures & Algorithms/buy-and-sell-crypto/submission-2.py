class Solution:
    def maxProfit(self,prices):
        maxprof = []
        temp = []
        j = len(prices) - 1
        if j+1 == 1 or j == 0: 
            return 0

        for i in range(len(prices)): 
            print(maxprof)
            while j > i:
                temp.append(prices[j] - prices[i])
                print(temp)
                maxprof.append(max(temp))
                print(maxprof)
                j -= 1
            j = len(prices) - 1
        
        n = max(maxprof)
        if n < 0: 
            return 0
        else:
            return n