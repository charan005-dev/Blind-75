#TC: O(n)
#SC: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        
        
        #two pointers where left pointer will be the day we buy the stocks and the right pointer will be the day we sell 
        
        #update two of the pointers when left is higher than right pointer 
        
        #if right pointer is higher than the left pointer, then update the profit 
        
        l,r=0,1 
        maxprofit = 0 
        
        while r < len(prices): 
            
            if prices[l] < prices[r]: 
                profit = prices[r] - prices[l] 
                maxprofit = max(maxprofit, profit)
            else: 
                l=r 
            r+=1 
            
        return maxprofit
                
                
        
            
        